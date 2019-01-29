from unittest import mock

from helpers import BaseHelper


@mock.patch('helpers.get_response')
def test_get_site_status_without_autospec(mocked_get_response):
    mocked_get_response.return_value.json.return_value = {"result": True}
    mocked_get_response.return_value.status_code = 200
    result = BaseHelper.get_site_status("http://non-existent-url")
    assert result == {"code": 200}


@mock.patch('helpers.get_response', autospec=True)
def test_get_site_status_with_autospec(mocked_get_response):
    mocked_get_response.return_value.json.return_value = {"result": True}
    mocked_get_response.return_value.status_code = 200
    result = BaseHelper.get_site_status("http://non-existent-url")
    assert result == {"code": 200}
