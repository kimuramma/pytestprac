import requests
import pytest


@pytest.fixture()
def access_token():
    credentials = {
    "username": "samsung@ffin.credit",
    "password": "7F]{mJbHr%F=QrY"
    }
    response = requests.post('https://fastcash-back.trafficwave.kz/ffc-api-auth/', json=credentials)
    print(response)

    assert response.status_code == 200

    if response.status_code == 200:
        access_token = {'Authorization': 'JWT '+ response.json().get('access')}
        return access_token
    else:
        print('Ошибка аутентификации:', response.status_code)
        return None

def test_get_product(access_token):


    if access_token:
        headers = access_token

        response = requests.get('https://fastcash-back.trafficwave.kz/ffc-api-public/universal/general/products', headers = headers)
        if response.status_code == 200:
            print('Products has given')
            print(response.json())
        else:
            print('we are failed: ', response.status_code)

    else: print('cannot given access_token')


def test_apply_lead(access_token):
    headers = access_token
    req_body = {
    "iin": "940609301768",
    "mobile_phone": "+77474196207",
    "product": "SAMSUNG12",
    "partner": "SAMSUNG",
    "channel": "SAMSUNG_WEB",
    "uuid": "",
    "credit_params": {
        "period": 24,
        "principal": 150000,
        "interest_rate": 0,
        "effective_rate": 0,
        "monthly_payment": ""
    },
    "additional_information": {
        "hook_url": "",
        "success_url": "",
        "failure_url": "",
        "reference_id": "4sd65a4s5d4a",
        "delivery_address": ""
    },
    "email": "ksks555@mail.ru"
}
    response = requests.post(
        'https://fastcash-back.trafficwave.kz/ffc-api-public/universal/apply/apply-lead',
        json = req_body,
        headers = headers
    )
    print(response.json())
    assert response.status_code == 202
    if response.status_code == 202:
        uuid = response.json().get('uuid')
        return uuid
    else:
        print('uuid не был получен')