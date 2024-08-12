import requests


class Model2:
    response = None
    response_json = None

    def get_model2(self, headers):
        self.response = requests.get('https://fastcash-back.trafficwave.kz/ffc-api-public/universal/datalab/model2/701225401572', headers=headers)
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code == 200

