import requests


def get_response(url, method, data=None):
    header = {"Authorization": "FAKE_TOKEN", "content-type": "application/json"}
    request_method = getattr(requests, method)
    response = request_method(url=url, headers=header, data=data)
    return response
