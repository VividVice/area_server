import requests

def get_server_ip():
    response = requests.get("https://ipinfo.io")
    return response.json()["ip"]