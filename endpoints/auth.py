import requests


class Auth:
    response = None
    response_json = None
    access_token = None

    def get_token(self, credentials):
        self.response = requests.post("https://fastcash-back.trafficwave.kz/ffc-api-auth/", json=credentials)
        self.response_json = self.response.json()
        self.access_token = {"Authorization": "JWT '+self.response_json.get('access')"}

    def check_response_is_200(self):
        assert self.response.status_code == 200