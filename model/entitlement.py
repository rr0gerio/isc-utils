import certifi
import requests
from model.config import ConfigModel


class EntitlementModel:
    def __init__(self, token):
        self.config = ConfigModel()
        self.token = token

    def find_entitlement(self, source_id, entitlement_name):

        if "&" in entitlement_name:
            name_convert = entitlement_name.replace("&", "%26")
        else:
            name_convert = entitlement_name

        url = (f'https://{self.config["environment"]["tenant"]}.api.identitynow.com/beta/entitlements?filters=source'
               f'.id%20eq%20"{source_id}"%20and%20name%20eq%20"{name_convert}"')

        header = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        try:
            response = requests.request("GET", url, headers=header, verify=certifi.where())

            if response.status_code == 200 and response.text != '[]':
                return response.json()[0]['id']
            else:
                print("Entitlement não encontrado." + entitlement_name)
                response.json()

        except Exception as Error:
            print(f"Error to get Entitlement: {Error}")
