from sys import path
from os import getenv
path.append('../..')
from modules.config.config import Config
from modules.database.DB import UserModel
from requests import request
from typing import Dict


class GitHubAPI:

    def __init__(self, user: UserModel) -> None:
        self.user = user
        self.oauth_token = user.user_services.get("github", {}).get("access_token")

    def create_auth_header(self) -> Dict[str, str]:
        if not self.oauth_token:
            return {}
        return {
            "Authorization": f"Bearer {self.oauth_token}"
        }

    def make_github_api_request(self, method: str, endpoint: str, data=None):
        base_url = "https://api.github.com"
        url = f"{base_url}{endpoint}"
        headers = self.create_auth_header()
        response = request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_user_repositories(self):
        return self.make_github_api_request("GET", "/user/repos")

    def get_repository_details(self, repo_owner, repo_name):
        endpoint = f"/repos/{repo_owner}/{repo_name}"
        return self.make_github_api_request("GET", endpoint)

    def create_repository(self, repo_name, private=False):
        data = {
            "name": repo_name,
            "private": private
        }
        return self.make_github_api_request("POST", "/user/repos", data)

    def create_issue(self, repo_owner, repo_name, title, body):
        endpoint = f"/repos/{repo_owner}/{repo_name}/issues"
        data = {
            "title": title,
            "body": body
        }
        return self.make_github_api_request("POST", endpoint, data)

    def create_comment(self, repo_owner, repo_name, issue_number, body):
        endpoint = f"/repos/{repo_owner}/{repo_name}/issues/{issue_number}/comments"
        data = {
            "body": body
        }
        return self.make_github_api_request("POST", endpoint, data)


def get_github_email(access_token):
    url = "https://api.github.com/user/emails"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = request("GET", url, headers=headers)
    response.raise_for_status()
    return response.json()[0]["email"]