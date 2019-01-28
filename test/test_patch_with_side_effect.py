from unittest import mock, TestCase
from unittest.mock import Mock

from requests.exceptions import RequestException

from helpers import BaseHelper

response_200 = Mock(status_code=200, json=Mock(return_value={"code": 200}))
response_400 = Mock(status_code=400, json=Mock(return_value={"code": 400}))


def side_effect(url):
    if url == "http://raise-error.com":
        raise RequestException
    result_dict = {
        "http://response-200.com": response_200,
        "http://response-400.com": response_400,
    }
    return result_dict[url]


class MockWithSideEffect(TestCase):
    @mock.patch('helpers.get_response')
    def test_function_side_effect(self, mocked_get_response):
        mocked_get_response.side_effect = side_effect
        result = BaseHelper.get_site_status("http://response-200.com")
        assert result == {"code": 200}
        result = BaseHelper.get_site_status("http://response-400.com")
        assert result == {"code": 400}
        result = BaseHelper.get_site_status("http://raise-error.com")
        assert result == {"code": None}

    @mock.patch('helpers.get_response')
    def test_iterable_side_effect(self, mocked_get_response):
        mocked_get_response.side_effect = [response_200, response_400, RequestException]
        result = BaseHelper.get_site_status("http://response-200.com")
        assert result == {"code": 200}
        result = BaseHelper.get_site_status("http://response-400.com")
        assert result == {"code": 400}
        result = BaseHelper.get_site_status("http://raise-error.com")
        assert result == {"code": None}
