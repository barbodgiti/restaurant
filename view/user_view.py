from tkinter import *
from view.commponent import *
from tkinter import ttk


class UserView:
    def __init__(self):
        self.window = Tk()
        self.window.title("RESTAURANT")
        self.window.geometry("500x500")


        food = EntryWithBarel(self.window, "food", 20,160)










        self.window.mainloop()