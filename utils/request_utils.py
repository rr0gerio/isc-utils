import requests
import certifi
from utils.logger_utils import log


class RequestUtils: 
    @staticmethod
    def request(url, method = "GET", headers=None, data=None, params=None, json=None):
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                params=params,
                json=json,
                verify=certifi.where()
            )
            if response.status_code in [200, 201]:
                log.info(f"Request successful: {method} {url}")
                return response.json()
            else:
                log.error(f"Request failed {response.status_code}: {response.json()}")
        except requests.exceptions.RequestException as error:
            log.error(f"Request exception for {url}: {error}")
        return None
