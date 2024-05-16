import csv
from model.access_profile import AccessProfile
from utils.config_manager import ConfigManager
from model.authentication import AuthenticationModel
from model.csv import CSVModel

class AccessProfileController:
    def __init__(self):
        self.token = None
        self.api = None
        self.config = ConfigManager().config
        self.csv_model = CSVModel(self.config["environment"]["access_profile_file"])

    def authenticate(self):
        authentication_api = AuthenticationModel()
        self.token = authentication_api.get_token()
        if not self.token:
            return False
        self.api = AccessProfile(self.token)
        return True

    def bulk_create_access_profile(self):
        access_profiles = self.csv_model.get_unique_values_for_column("AccessProfileName")

        if not access_profiles:
            print("Error: No access profiles found in CSV file.")
            return None

        access_profiles_ids = []
        for access_profile_name in access_profiles:
            matching_rows = self.csv_model.get_rows_matching_column_value("AccessProfileName", access_profile_name)

            if not matching_rows:
                print(f"Error: No matching rows found for Access Profile {access_profile_name}.")
                continue

            payload = self._create_payload(matching_rows)
            access_profile_id = self.api.create_access_profile(payload)
            if access_profile_id:
                access_profiles_ids.append(access_profile_id)
            else:
                print(f"Error: Failed to create Access Profile for {access_profile_name}.")
        return access_profiles_ids

    def _create_payload(self, matching_rows):
        # Implementar a lógica para criar o payload com base nos dados das linhas correspondentes do CSV
        # Aqui você pode usar as informações das linhas correspondentes do CSV para construir o payload conforme necessário
        # Certifique-se de lidar com casos especiais, como múltiplos owners, aprovações de grupo de governança, etc.
        approval_schemes
        payload = {}
        return payload
