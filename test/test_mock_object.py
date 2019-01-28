from unittest import mock
from unittest.mock import Mock

import requests

fake_response = Mock(
    json=Mock(return_value={"result": True}),
    status_code=200
)


# @mock.patch('patch할 module의 path', return_value='해당 module의 호출 결과')
@mock.patch('requests.get', return_value=fake_response)
def test_mock_patch(mocked_requests_get):
    response = requests.get("http://non-existent-url")
    assert response.json() == {"result": True}
    assert response.status_code == 200
