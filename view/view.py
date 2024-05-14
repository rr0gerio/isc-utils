from controller.controller import AccessProfileController

class AccessProfileCLI:
    def __init__(self):
        self.controller = AccessProfileController()

    def display_menu(self):
        print("Welcome to Access Profile Manager")
        print("1. Create Access Profile")
        print("2. Exit")

    def create_access_profile(self):
        profile_name = input("Enter Access Profile Name: ")
        if not profile_name:
            print("Error: Please enter a profile name")
            return

        if not self.controller.authenticate():
            print("Error: Authentication failed. Check logs for details.")
            return

        payload = {
            "name": profile_name,
            # Adicione outros campos do payload conforme necessário
        }
        access_profile_id = self.controller.create_access_profile(payload)
        if access_profile_id:
            print(f"Success: Access Profile created with ID: {access_profile_id}")
        else:
            print("Error: Failed to create Access Profile. Check logs for details.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_access_profile()
            elif choice == "2":
                print("Exiting Access Profile Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli = AccessProfileCLI()
    cli.run()
