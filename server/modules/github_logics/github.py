import requests

username = "REBELO-luc "
token = "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"

repo_name = "NewRepoNamee"

url = f"https://api.github.com/user/repos"

data = {
    "name": repo_name,
    "description": "Hello",
    "private": True,
}

headers = {
    "Authorization": f"token {token}",
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully!")
else:
    print(f"Failed to create repository. Status code: {response.status_code}")
    print(response.json())
