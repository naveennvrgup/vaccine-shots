import pytest
from main import get_bangalore_vaccine_slots, BASE_URL

def test_all_call_succeed(requests_mock):
    requests_mock.get(f'{BASE_URL}/api/v2/appointment/sessions/public/findByPin', json={'sessions':[{
        'center_id': 234,
        'name': 'test',
        'slots': ['testlost']
    }]})
    actual = get_bangalore_vaccine_slots('05-05-2021',['213423'])
    print(actual)
    assert actual == [{
        'center_id': 234,
        'name': 'test',
        'slot': 'testlost'
    }]