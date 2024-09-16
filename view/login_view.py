from tkinter import *
import tkinter.messagebox as msg

from controller.user_controller import UserController
from view.commponent import EntryWithBarel
from view.user_view import *

class LoginView:
    def __init__(self):
        self.window = Tk()
        self.window.title('LOGIN')
        self.window.config(bg="palegreen3")
        self.window.geometry('500x500')

        self.username = EntryWithBarel(self.window, "Username", 60, 180,120)
        self.password = EntryWithBarel(self.window, "Password", 60, 220,120)

        Button(self.window, text="LOGIN", width=20, command=self.login_click).place(x=120, y=300)

        self.window.mainloop()

    def login_click(self):
        status, message= UserController.find_by_username_and_password(self.username.get(), self.password.get())
        if status:
            msg.showinfo('LOGIN', "Login Successful")
            self.window.destroy()
            user_view = UserView()
        else:
            msg.showerror('LOGIN', "Login Failed")

