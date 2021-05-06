import pytest
from main import get_bangalore_vaccine_slots, BASE_URL
from test_data import all_calls_succeed, some_calls_5xx, some_calls_timeout


query_url = f'{BASE_URL}/api/v2/appointment/sessions/public/findByPin'


@pytest.mark.parametrize('date,pincodes,api_responses,expected', all_calls_succeed.data)
def test_all_call_succeed(requests_mock, date, pincodes, api_responses, expected):
    requests_mock.get(query_url, api_responses)
    actual = get_bangalore_vaccine_slots(date,pincodes)

    assert actual == expected


@pytest.mark.parametrize('date,pincodes,api_responses,expected', some_calls_5xx.data)
def test_some_calls_5xx(requests_mock, date, pincodes, api_responses, expected):
    requests_mock.get(query_url, api_responses)
    actual = get_bangalore_vaccine_slots(date,pincodes)
    
    assert actual == expected

