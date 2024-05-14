import yaml
import csv
import requests

class ConfigModel:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
        return config

class IdentityNowAPI:
    def __init__(self, jwt_token):
        self.token = jwt_token

    def get_source_id(self, sourceName):
        url = f'https://{self.config["environment"]["tenant"]}.api.identitynow.com/v3/sources?filters=name%20eq%20"{sourceName}"'

        header = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        try:
            response = requests.request("GET", url, headers=header, verify=False)

            if response.status_code == 200:
                return response.json()[0]['id']
            else:
                print(response.json())

        except Exception as Error:
            print(f"Error to get Source: {sourceName}")

    def get_entitlement_id(self, sourceId, entitlementName):

        if "&" in entitlementName:
            name_convert = entitlementName.replace("&", "%26")
        else:
            name_convert = entitlementName

        url = f'https://{self.config["environment"]["tenant"]}.api.identitynow.com/beta/entitlements?filters=source.id%20eq%20"{sourceId}"%20and%20name%20eq%20"{name_convert}"'

        header = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        try:
            response = requests.request("GET", url, headers=header, verify=False)

            if response.status_code == 200 and response.text != '[]':
                return response.json()[0]['id']
            else:
                print("Entitlement não encontrado." + entitlementName)
                response.json()

        except Exception as Error:
            print(f"Error to get Entitlement: {Error}")

    def get_identity_id(self, mail):
        try:
            url = f'https://{self.config["environment"]["tenant"]}.api.identitynow.com/v3/search'

            header = {
                "Accept": "application/json",
                "Authorization": f"Bearer {self.token}"
            }
            payload = {
                "queryType": "SAILPOINT",
                "indices": ["identities"],
                "query": {
                    "query": f"attributes.email:{mail}"  # Corrigido aqui
                },
                "queryResultFilter": {
                    "includes": ["id", "name", "displayName"]
                }
            }

            response = requests.post(url, headers=header, json=payload, verify=False)  # Usando json em vez de data
            response_data = response.json()

            if response.status_code == 200:
                return response_data[0]
            else:
                print(f"Erro na resposta: {response_data}")
        except requests.exceptions.RequestException as Error:
            print(f"Erro ao obter identidade {mail}. Erro: {Error}")

    def create_access_profile(self, payload):
        url = f"https://{self.config['environment']['tenant']}.api.identitynow.com/v3/access-profiles"

        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        print("creating access profile")
        response = requests.request("POST", url=url, headers=header, data=json.dumps(payload), verify=False)
        
        if response.status_code == 200 or response.status_code == 201:
            print(f"Access Profile criado: {payload.get('name')}")
            return response.json()['id']
        else:
            return None
