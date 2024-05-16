import requests
import certifi
from model.config import ConfigModel


class AccessProfile:
    def __init__(self, token):
        self.config = ConfigModel()
        self.token = token

    def create_access_profile(self, payload):
        url = f"https://{self.config['environment']['tenant']}.api.identitynow.com/v3/access-profiles"

        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.request("POST", url=url, headers=header, json=payload, verify=certifi.where())
        if response.status_code == 200 or response.status_code == 201:
            return response.json()['id']
        else:
            return None
