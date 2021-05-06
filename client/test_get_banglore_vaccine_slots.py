import pytest
import requests
from main import get_bangalore_vaccine_slots, BASE_URL
from test_data import all_calls_succeed, some_calls_5xx, some_calls_timeout
from requests.exceptions import Timeout, HTTPError

query_url = f'{BASE_URL}/api/v2/appointment/sessions/public/findByPin'

# exampel response
# response_1 = {
#     'json': {'sessions':[{
#         'center_id': 234,
#         'name': 'APPLE TEST',
#         'slots': ["09:00AM-11:00AM",'01:00PM-02:00PM']
#     }]},
#     'status_code': 200
# }
@pytest.mark.parametrize('date,pincodes,api_responses,expected', all_calls_succeed.data)
def test_all_call_succeed(requests_mock, date, pincodes, api_responses, expected):
    requests_mock.get(query_url, api_responses)
    actual = get_bangalore_vaccine_slots(date,pincodes)

    assert expected == actual

class MockResponse:
    def __init__(self, response):
        self.response = response

    def json(self):
        return self.response
    
    def raise_for_status(self):
        if type(self.response) in (HTTPError, Timeout):
            raise self.response

def convert_responses(responses):
    return [MockResponse(x) for x in responses]  


@pytest.mark.parametrize('date,pincodes,api_responses,expected', some_calls_5xx.data + some_calls_timeout.data)
def test_some_calls_5xx_or_timeout(mocker, date, pincodes, api_responses, expected):
    converted_api_responses = convert_responses(api_responses)
    mocker.patch('requests.get', side_effect = converted_api_responses)
    actual = get_bangalore_vaccine_slots(date,pincodes)
    
    assert expected == actual


def test_all_calls_timeout(mocker):
    mocker.patch('requests.get', side_effect=Timeout)
    get_bangalore_vaccine_slots('05-05-2021',['560116','562106','562135','562110'])


def mock_get(url, headers, timeout):
    raise Timeout()

def test_all_calls_5xx(monkeypatch):
    monkeypatch.setattr(requests,'get',mock_get)
    get_bangalore_vaccine_slots('05-05-2021',['560116','562106','562135','562110'])
