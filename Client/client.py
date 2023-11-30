import clientClass
import userClass
import messageClass
import tkinter as tk
from tkinter import messagebox

class client:
    def __init__(self):
        pass
    def register_user(self):
        messagebox.showinfo("Register", "New user registered")

    def login(self):
        messagebox.showinfo("Login", "User logged in")
        landing_page.destroy()

    def exit_program(self):
        landing_page.destroy()
    
    def landingPage(self):
        global landing_page
        landing_page = tk.Tk()
        landing_page.title("Login Page")

        label_username = tk.Label(landing_page, text="Username:")
        label_password = tk.Label(landing_page, text="Password:")
        entry_username = tk.Entry(landing_page)
        entry_password = tk.Entry(landing_page, show="*")  # Show asterisks for password
        button_login = tk.Button(landing_page, text="Login", command=self.login)
        button_register = tk.Button(landing_page, text="Register", command=self.register_user)
        button_exit = tk.Button(landing_page, text="Exit", command=self.exit_program)

        label_username.grid(row=0, column=0, sticky=tk.E)
        label_password.grid(row=1, column=0, sticky=tk.E)
        entry_username.grid(row=0, column=1)
        entry_password.grid(row=1, column=1)
        button_login.grid(row=2, column=0, columnspan=2, pady=5)
        button_register.grid(row=3, column=0, columnspan=2, pady=5)
        button_exit.grid(row=4, column=0, columnspan=2, pady=5)

        landing_page.mainloop()
        

if __name__ == "__main__":
    test = client()
    test.landingPage()
    