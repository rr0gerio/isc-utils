import tkinter as tk
from tkinter import messagebox
from controller.controller import AccessProfileController

class AccessProfileView:
    def __init__(self):
        self.controller = AccessProfileController()

        self.root = tk.Tk()
        self.root.title("Access Profile Manager")

        self.label = tk.Label(self.root, text="Access Profile Name:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Create Access Profile", command=self.create_access_profile)
        self.button.pack()

    def create_access_profile(self):
        profile_name = self.entry.get()
        if not profile_name:
            messagebox.showerror("Error", "Please enter a profile name")
            return

        if not self.controller.authenticate():
            messagebox.showerror("Error", "Authentication failed. Check logs for details.")
            return

        payload = {
            "name": profile_name,
            # Adicione outros campos do payload conforme necessário
        }
        access_profile_id = self.controller.create_access_profile(payload)
        if access_profile_id:
            messagebox.showinfo("Success", f"Access Profile created with ID: {access_profile_id}")
        else:
            messagebox.showerror("Error", "Failed to create Access Profile. Check logs for details.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    view = AccessProfileView()
    view.run()
