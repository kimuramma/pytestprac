import requests
import pytest
from endpoints.auth import Auth
from endpoints.get_products import Products
from endpoints.model2 import Model2


@pytest.fixture()
def access_token():
    auth_endpoint = Auth()
    credentials = {
        "username": "samsung@ffin.credit",
        "password": "7F]{mJbHr%F=QrY"
    }
    auth_endpoint.access_token
    auth_endpoint.get_token(credentials=credentials)
    auth_endpoint.check_response_is_200()
    return auth_endpoint.access_token


def test_get_product(access_token):
    products = Products()
    products.get_product(access_token=access_token)
    products.check_response_is_200()


def test_get_model2(access_token):
    model2 = Model2()
    model2.get_model2(headers=access_token)
    model2.check_response_is_200()


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
        json=req_body,
        headers=headers
    )
    print(response.json())
    assert response.status_code == 202
    if response.status_code == 202:
        uuid = response.json().get('uuid')
        return uuid
    else:
        print('uuid не был получен')
