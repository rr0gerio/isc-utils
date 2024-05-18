from model.config_model import ConfigModel
from typing import TypedDict
from utils.logger_utils import log

class GroupInfo(TypedDict):
    group_name: str
    description: str
    owner_id: str
    owner_name: str

class GovernanceGroup:
    def __init__(self, token) -> None:
        self.config = ConfigModel()
        self.token = token

    def create_governance_group(self, group_info: GroupInfo):
        url = f'https://{self.config["environment"]["tenant"]}.api.identitynow.com/beta/workgroups'
        payload = {
            "owner": {
                "type": "IDENTITY",
                "id": group_info.group_name ,
                "name": group_info.owner_name
            },
            "name": group_info.group_name,
            "description": group_info.description
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = self._request("POST", url, headers=headers, data=json.dumps(payload))

        if response:
            log.info(f"Governance group '{group_name}' created successfully.")
            return response['id']
        else:
            log.error(f"Failed to create governance group '{group_name}'.")
            return None
