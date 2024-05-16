import requests
from model.config import ConfigModel

class SourceAPI:
    def __init__(self, token):
        self.config = ConfigModel()
        self.token = token

    def get_source_by_name(config, token, sourceName):
        url = f'https://{config["environment"]["tenant"]}.api.identitynow.com/v3/sources?filters=name%20eq%20"{sourceName}"'

        header = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        try:
            response = requests.request("GET", url, headers=header, verify=False)

            if response.status_code == 200:
                return response.json()[0]['id']
            else:
                print(response.json())

        except Exception as Error:
            print(f"Error to get Source: {sourceName}")