from requests.exceptions import Timeout

session_1 = {
    'sessions':[{
        'center_id': 234,
        'name': 'APPLE TEST',
        'slots': ["09:00AM-11:00AM",'01:00PM-02:00PM']
    }]}

session_2 ={ 
    'sessions': [{
        'center_id': 546,
        'name': 'BANANNA SYRUP',
        'slots': ["12:00AM-01:00PM"]
    }]}

no_session = {
    'sessions': []
}

date = '05-05-2021'

pincodes = [
    560116,
    562106,
    562135,
    562110
]

api_responses_case1_no_available = [
    no_session,
    no_session,
    Timeout(),
    no_session,
]

api_responses_case2_1slot_available = [
    no_session,
    session_2,
    Timeout(),
    no_session,
]

api_responses_case3_3slots_available = [
    session_1,
    session_2,
    Timeout(),
    Timeout(),
]

expected_case1_no_available = []

expected_case2_1slot_available = [{
            'center_id': 546,
            'name': 'BANANNA SYRUP',
            'slot':"12:00AM-01:00PM"
        }]

expected_case3_3slots_available = [{
            'center_id': 234,
            'name': 'APPLE TEST',
            'slot':"09:00AM-11:00AM"
        },{
            'center_id': 234,
            'name': 'APPLE TEST',
            'slot':'01:00PM-02:00PM'
        },{
            'center_id': 546,
            'name': 'BANANNA SYRUP',
            'slot':"12:00AM-01:00PM"
        }]

data = [
    (
        date,
        pincodes,
        api_responses_case1_no_available,
        expected_case1_no_available
    ),
    (
        date,
        pincodes,
        api_responses_case2_1slot_available,
        expected_case2_1slot_available
    ),
    (
        date,
        pincodes,
        api_responses_case3_3slots_available,
        expected_case3_3slots_available
    ),
]
