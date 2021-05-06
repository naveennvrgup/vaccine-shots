import requests
import argparse

BASE_URL = 'https://cdn-api.co-vin.in'
BASE_URL = 'http://localhost:5000'

def get_api_helper(date, pincode):

    headers = {
        'Accept-Language': 'en_US',
        'Accept': 'application/json'
    }

    query_url = f'{BASE_URL}/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
    response = requests.get(query_url, headers=headers, timeout=2)
    response.raise_for_status()

    return response.json()


def get_bangalore_vaccine_slots(date, pincodes):

    slots = []

    for pincode in pincodes:
        try:
            response = get_api_helper(date, pincode)
            sessions_by_pincode = response['sessions']

            for session in sessions_by_pincode:
                slots_by_center = [{
                    'center_id': session['center_id'], 
                    'name': session['name'], 
                    'slot': y} for y in session['slots']]
                slots.extend(slots_by_center)
        except (requests.exceptions.Timeout):
            pass

    return slots


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Query vaccine slots by date and pincodes')
    parser.add_argument('-d', '--date', required=True,
                        help='date to query as DD-MM-YYYY')
    parser.add_argument('-p', '--pincodes', required=True, nargs='+',
                        default=[], help='space separated list of 6 digit pincodes')
    args = parser.parse_args()

    print(get_bangalore_vaccine_slots(args.date, args.pincodes))
