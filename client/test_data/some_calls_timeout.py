# session_1 = {
#     'sessions':[{
#         'center_id': 234,
#         'name': 'APPLE TEST',
#         'slots': ["09:00AM-11:00AM",'01:00PM-02:00PM']
#     }]}

# session_2 ={ 
#     'sessions': [{
#         'center_id': 546,
#         'name': 'BANANNA SYRUP',
#         'slots': ["12:00AM-01:00PM"]
#     }]}

no_session = {
    'sessions': []
}


# response_1 = {
#     'json': session_1,
#     'status_code': 200
# }

# response_1_3_seconds = {
#     'json': session_1,
#     'status_code': 200
# }

# response_2 = {
#     'json': session_2,
#     'status_code': 200
# }

response_no_session = {
    'json': no_session,
    'status_code': 200
}

date = '05-05-2021'

pincodes = [
    560116,
    562106,
    562135,
    562110
]

api_responses_case1_1_timeout = [
    response_no_session,
    response_no_session,
    response_no_session,
    response_no_session,
]

# api_responses_case2_1slot_available = [
#     response_no_session,
#     response_2,
#     response_no_session,
#     response_no_session,
# ]

# api_responses_case3_3slots_available = [
#     response_1,
#     response_2,
#     response_no_session,
#     response_no_session,
# ]

expected_case1_1_timeout = []

# expected_case2_1slot_available = [{
#             'center_id': 546,
#             'name': 'BANANNA SYRUP',
#             'slot':"12:00AM-01:00PM"
#         }]

# expected_case3_3slots_available = [{
#             'center_id': 234,
#             'name': 'APPLE TEST',
#             'slot':"09:00AM-11:00AM"
#         },{
#             'center_id': 234,
#             'name': 'APPLE TEST',
#             'slot':'01:00PM-02:00PM'
#         },{
#             'center_id': 546,
#             'name': 'BANANNA SYRUP',
#             'slot':"12:00AM-01:00PM"
#         }]

data = [
    (
        date,
        pincodes,
        api_responses_case1_1_timeout,
        expected_case1_1_timeout
    ),
]
