# test_base_helper.py
from unittest import mock
from unittest.mock import Mock

from helpers import BaseHelper

mocked_response = Mock(
    json=Mock(return_value={"result": True}),
    status_code=200
)


@mock.patch('helpers.get_response', return_value=mocked_response)
def test_get_response_with_return_value_kwarg(mocked_get_response):
    result = BaseHelper.get_site_status("http://non-existent-url")
    assert result == {"code": 200}


@mock.patch('helpers.get_response', new=Mock(return_value=mocked_response))
def test_get_response_with_new_kwarg():
    result = BaseHelper.get_site_status("http://non-existent-url")
    assert result == {"code": 200}
