from view.config_view import ConfigView
from view.access_profile_view import AccessProfileView
from utils.config_manager_utils import ConfigManager
from utils.terminal_utils import terminal


class MenuView:
    def __init__(self) -> None:
        self.config_manager = ConfigManager()

    def display_menu(self):
        print("Welcome to ISC Toolbox")
        print("1. Manage Access Profiles")
        print("2. Insert tenant config")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                access_profile_view = AccessProfileView()
                access_profile_view.run()
            elif choice == "2":
                config_view = ConfigView()
                config_view.prompt_for_config()
            elif choice == "3":
                break
            else:
                print("Invalid option!")


if __name__ == "__main__":
    menu = MenuView()
    menu.run()
