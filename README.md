# Vaccine shots

Code present in `client/main.py`

Tests are present in `client/test_get_banglore_vaccine_slots.py`

Pytest plugins used:
1. pytest-cov
1. pytest-mock
2. requests-mock

## Setup

```
cd client
virtualenv env -p python3.8
source env/bin/activate
pip install -r requirements.txt
```

## Usage
```
python main.py -h
usage: main.py [-h] -d DATE -p PINCODES [PINCODES ...]

Query vaccine slots by date and pincodes

optional arguments:
  -h, --help            show this help message and exit
  -d DATE, --date DATE  date to query as DD-MM-YYYY
  -p PINCODES [PINCODES ...], --pincodes PINCODES [PINCODES ...]
                        space separated list of 6 digit pincodes

```
## Run Tests

```
# via docker
cd client
docker build -t client .
docker run client

# or 
bash docker_test.sh

# without docker
pytest --cov -vv
```
## Example output
```
========================================================================= test session starts ==========================================================================
platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /home/naveennvrgup/projects/vaccine-shots/client/env/bin/python
cachedir: .pytest_cache
rootdir: /home/naveennvrgup/projects/vaccine-shots/client
plugins: requests-mock-1.9.2, mock-3.6.0, cov-2.11.1
collected 11 items                                                                                                                                                     

test_get_banglore_vaccine_slots.py::test_all_call_succeed[05-05-2021-pincodes0-api_responses0-expected0] PASSED                                                  [  9%]
test_get_banglore_vaccine_slots.py::test_all_call_succeed[05-05-2021-pincodes1-api_responses1-expected1] PASSED                                                  [ 18%]
test_get_banglore_vaccine_slots.py::test_all_call_succeed[05-05-2021-pincodes2-api_responses2-expected2] PASSED                                                  [ 27%]
test_get_banglore_vaccine_slots.py::test_some_calls_5xx_or_timeout[05-05-2021-pincodes0-api_responses0-expected0] PASSED                                         [ 36%]
test_get_banglore_vaccine_slots.py::test_some_calls_5xx_or_timeout[05-05-2021-pincodes1-api_responses1-expected1] PASSED                                         [ 45%]
test_get_banglore_vaccine_slots.py::test_some_calls_5xx_or_timeout[05-05-2021-pincodes2-api_responses2-expected2] PASSED                                         [ 54%]
test_get_banglore_vaccine_slots.py::test_some_calls_5xx_or_timeout[05-05-2021-pincodes3-api_responses3-expected3] PASSED                                         [ 63%]
test_get_banglore_vaccine_slots.py::test_some_calls_5xx_or_timeout[05-05-2021-pincodes4-api_responses4-expected4] PASSED                                         [ 72%]
test_get_banglore_vaccine_slots.py::test_some_calls_5xx_or_timeout[05-05-2021-pincodes5-api_responses5-expected5] PASSED                                         [ 81%]
test_get_banglore_vaccine_slots.py::test_all_calls_timeout PASSED                                                                                                [ 90%]
test_get_banglore_vaccine_slots.py::test_all_calls_5xx PASSED                                                                                                    [100%]

----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name      Stmts   Miss  Cover
-----------------------------
main.py      31      8    74%
-----------------------------
TOTAL        31      8    74%


========================================================================== 11 passed in 0.13s ==========================================================================
```
## Example CLI usage
```
python main.py -d 05-05-2021 -p 562135 569399 
+--------+-----------+-------------+--------------------------+-----------------+
|   s.no |   pincode |   center_id | name                     | slot            |
|--------+-----------+-------------+--------------------------+-----------------|
|      1 |    562135 |      672926 | Chanraypatna Sub Centre  | 09:00AM-11:00AM |
|      2 |    562135 |      672926 | Chanraypatna Sub Centre  | 11:00AM-01:00PM |
|      3 |    562135 |      672926 | Chanraypatna Sub Centre  | 01:00PM-03:00PM |
|      4 |    562135 |      672926 | Chanraypatna Sub Centre  | 03:00PM-06:00PM |
|      5 |    562135 |      246830 | Yaliyuru Subcentre       | 09:00AM-11:00AM |
|      6 |    562135 |      246830 | Yaliyuru Subcentre       | 11:00AM-01:00PM |
|      7 |    562135 |      246830 | Yaliyuru Subcentre       | 01:00PM-03:00PM |
|      8 |    562135 |      246830 | Yaliyuru Subcentre       | 03:00PM-06:00PM |
|      9 |    562135 |      246802 | Gurappanamata Sub Centre | 09:00AM-11:00AM |
|     10 |    562135 |      246802 | Gurappanamata Sub Centre | 11:00AM-01:00PM |
|     11 |    562135 |      246802 | Gurappanamata Sub Centre | 01:00PM-03:00PM |
|     12 |    562135 |      246802 | Gurappanamata Sub Centre | 03:00PM-06:00PM |
+--------+-----------+-------------+--------------------------+-----------------+

```