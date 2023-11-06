import requests

username = "REBELO-luc"
token = "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"

repo_name = "NewRepoName"

url = f"https://api.github.com/repos/{username}/{repo_name}"

headers = {
    "Authorization": f"token {token}",
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print(f"Repository '{repo_name}' deleted successfully!")
else:
    print(f"Failed to delete repository. Status code: {response.status_code}")
    print(response.json())