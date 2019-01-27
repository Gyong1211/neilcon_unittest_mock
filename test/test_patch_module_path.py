from unittest import mock, TestCase

from helpers import BaseHelper


class PatchModulePathTest(TestCase):

    @mock.patch('utils.get_response')
    def test_잘못된_module_path(self, mocked_response):
        mocked_response.return_value.json.return_value = {"result": True}
        mocked_response.return_value.status_code = 200
        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result == {"code": 200}

    @mock.patch('helpers.get_response')
    def test_올바른_module_path(self, mocked_response):
        mocked_response.return_value.json.return_value = {"result": True}
        mocked_response.return_value.status_code = 200
        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result == {"code": 200}
