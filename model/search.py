import requests
from model.config import ConfigModel
from model.identity import Identity

class Search:
    def __init__(self, token):
        self.config = ConfigModel()
        self.token = token

    def get_identity_by_mail(self, mail):
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
                    "query": f"attributes.email:{mail}"
                },
                "queryResultFilter": {
                    "includes": ["id", "name", "displayName"]
                }
            }

            response = requests.post(url, headers=header, json=payload, verify=False)
            response_data = response.json()

            if response.status_code == 200:
                return Identity(response_data[0].get("id"))
            else:
                print(f"Erro na resposta: {response_data}")
        except requests.exceptions.RequestException as Error:
            print(f"Erro ao obter identidade {mail}. Erro: {Error}")
