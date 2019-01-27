from unittest import mock, TestCase
from unittest.mock import Mock

from helpers import BaseHelper


@mock.patch('helpers.get_response')
class UseMockPatchAsClassDecorator(TestCase):
    def test_클래스데코레이터로_사용(self, mocked_response):
        mocked_response.return_value.json.return_value = {"result": True}
        mocked_response.return_value.status_code = 200
        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result == {"code": 200}


class UseMockPatchAsMethodDecorator(TestCase):
    @mock.patch('helpers.get_response')
    def test_메서드데코레이터로_사용(self, mocked_response):
        mocked_response.return_value.json.return_value = {"result": True}
        mocked_response.return_value.status_code = 200
        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result == {"code": 200}


class UseMockPatchAsContextManager(TestCase):
    def test_컨텍스트매니저로_사용(self):
        mocked_response = Mock(json=Mock(return_value={"result": True}), status_code=200)
        with mock.patch('helpers.get_response', return_value=mocked_response):
            result = BaseHelper.get_site_status("http://non-existent-url")
            assert result == {"code": 200}
        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result != {"code": 200}


class TestUseMockPatchManually(TestCase):
    def test_수동으로_patch(self):
        patch_get_response = mock.patch('helpers.get_response')
        mocked_response = patch_get_response.start()  # get_response patch 시작
        mocked_response.return_value = Mock(json=Mock(return_value={"result": True}), status_code=200)
        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result == {"code": 200}
        patch_get_response.stop()  # get_response patch 종료

        result = BaseHelper.get_site_status("http://non-existent-url")
        assert result != {"code": 200}
