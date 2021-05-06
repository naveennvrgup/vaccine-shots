import requests
import argparse


def get_api_helper(date, pincode):
    BASE_URL = 'https://cdn-api.co-vin.in'
    BASE_URL = 'http://localhost:5000'

    headers = {
        'Accept-Language': 'en_US',
        'Accept': 'application/json'
    }

    query_url = f'{BASE_URL}/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
    response = requests.get(query_url, headers=headers, timeout=2)
    response.raise_for_status()
    
    return response.json()



def get_bangalore_vaccine_slots(date, pincodes):

    sessions = []

    for pincode in pincodes:
        try:
            response = get_api_helper(date, pincode)
            sessions_by_pincode = response['sessions']
            sessions.append({pincode: sessions_by_pincode})
        except (requests.exceptions.Timeout):
            sessions.append({pincode: None})

    return sessions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Query vaccine slots by date and pincodes')
    parser.add_argument('-d', '--date', required=True,
                        help='date to query as DD-MM-YYYY')
    parser.add_argument('-p', '--pincodes', required=True, nargs='+',
                        default=[], help='space separated list of 6 digit pincodes')
    args = parser.parse_args()

    print(get_bangalore_vaccine_slots(args.date, args.pincodes))
