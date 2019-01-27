import requests


def get_response(url):
    header = {"Authorization": "FAKE_TOKEN", "content-type": "application/json"}
    response = requests.get(url=url, headers=header)
    return response
