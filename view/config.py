import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import sys


class ConfigView:
    def prompt_for_config(self):
        print("Please enter the following details to create the configuration file:")

        if sys.stdin.isatty() and sys.stdout.isatty():
            # We're in an interactive terminal
            path_completer = PathCompleter(only_directories=False)
            access_profile_file = prompt("access_profile_file: ", completer=path_completer)
        else:
            # Fallback to simple input when not in an interactive terminal
            access_profile_file = input("access_profile_file: ")

        tenant = input("tenant: ")
        client_id = input("client_id: ")
        client_secret = input("client_secret: ")

        return {
            "environment": {
                "access_profile_file": access_profile_file,
                "tenant": tenant,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        }
