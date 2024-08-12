import requests


class Products:
    response = None
    response_json = None

    def get_product(self, access_token):
        self.response = requests.get('https://fastcash-back.trafficwave.kz/ffc-api-public/universal/general/products', headers=access_token)
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code == 200
