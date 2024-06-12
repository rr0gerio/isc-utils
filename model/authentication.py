import certifi
import requests
from utils.config_manager_utils import ConfigManager


class AuthenticationModel:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.config = self.config_manager.ensure_config()

    def get_token(self):
        client_id = self.config['environment']['client_id']
        client_secret = self.config['environment']['client_secret']
        tenant = self.config['environment']['tenant']

        url = f"https://{tenant}.api.identitynow.com/oauth/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        try:
            print(f"Authenticating to {tenant}")
            response = requests.post(url, data=payload, verify=certifi.where())

            if response.status_code == 200:
                print("Authenticated Successfully")
                return response.json()['access_token']
            elif response.status_code == 401:
                print("Authentication failed with status code 401.")
                self.update_config()
                return self.get_token()  # Try again with new credentials
            else:
                print(f"Error getting access token: code {response.status_code} with the message {response.json()}")

        except Exception as error:
            print(f"Unable to reach {url}, error: {error}")

        return None

    def update_config(self):
        new_config = self.config_manager.config_view.prompt_for_config()
        self.config_manager.config_model.save_config(new_config)
        self.config = new_config
