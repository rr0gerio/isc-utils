from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import sys


class ConfigView:
        
    def prompt_for_config(self):
        print("Please enter the following details to create the configuration file:")

        tenant = input("tenant: ")
        client_id = input("client_id: ")
        client_secret = input("client_secret: ")

        return {
            "environment": {
                "tenant": tenant,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        }

    def prompt_bulk_file_config(self, key_file_path):
        print("Please enter the following details to create the configuration file: ")

        if sys.stdin.isatty() and sys.stdout.isatty():
            # We're in an interactive terminal
            path_completer = PathCompleter(only_directories=False)
            bulk_load_file = prompt("access_profile: ", completer=path_completer)
        else:
            # Fallback to simple input when not in an interactive terminal
            bulk_load_file = input("access_profile: ")
        return {key_file_path:bulk_load_file}
    