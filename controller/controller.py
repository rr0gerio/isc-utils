import logging
from model.model import ConfigModel, IdentityNowAPI

class AccessProfileController:
    def __init__(self):
        self.environment = ConfigModel()
        self.token = None
        self.api = None

    def authenticate(self):
        self.token = self.get_token()
        if not self.token:
            logging.error("Failed to authenticate")
            return False
        self.api = IdentityNowAPI(self.token)
        return True

    def get_token(self):
        client_id = environment.config['environment']['client_id']
        client_secret = environment.config['environment']['client_secret']
        tenant = environment.config['environment']['tenant']

        url = f"https://{tenant}.api.identitynow.com/oauth/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        try:
            print(f"Authenticating to {tenant}")
            response = requests.post(url, data=payload, verify=False)

            if response.status_code == 200:
                print("Authenticated Successfully")
                return response.json()['access_token']
            else:
                print(f"Error getting access token: code {response.status_code} with the message {response.json()}")

        except Exception as error:
            print(f"Unable to reach {url}, error: {error} ")

        return None

    def create_access_profile(self, payload):
        if not self.token or not self.api:
            logging.error("Authentication required")
            return None
        
        return self.api.create_access_profile(payload)

    # Implemente outras operações de controle aqui
