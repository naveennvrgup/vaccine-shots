import requests
import argparse


def get_bangalore_vaccine_slots(date, pincodes):
    sessions = []

    for pincode in pincodes:
        query_url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
        response = requests.get(
            query_url, headers={'Accept-Language': 'en_US'})
        sessions.append(response)

    return temp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Query vaccine slots by date and pincodes')
    parser.add_argument('-d', '--date', required=True,
                        help='date to query as DD-MM-YYYY')
    parser.add_argument('-p', '--pincodes', required=True, nargs='+',
                        default=[], help='space separated list of 6 digit pincodes')
    args = parser.parse_args()

    print(get_bangalore_vaccine_slots(args.date, args.pincodes))
