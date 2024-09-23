from tkinter import *
from view.commponent import *
from view.component_tbl import *
from tkinter import ttk


class UserView:
    def __init__(self):
        self.window = Tk()
        self.window.title("RESTAURANT")
        self.window.geometry("1000x800")

        def food_tbl_click(row):
            print(row)

        def drink_tbl_click(row):
            print(row)

        def more_tbl_click(row):
            print(row)


        food_tbl = Table(self.window, ["Number","Food","Price"], [100,140,100], 20, 20, food_tbl_click)
        drink_tbl = Table(self.window, ["Number","Drink","Price"], [100,140,100], 530, 320, drink_tbl_click)
        more_tbl = Table(self.window, ["Number","More","Price"], [100,140,100], 530, 20, more_tbl_click)



        food_tbl.set_data()
        drink_tbl.set_data()
        more_tbl.set_data()

        self.window.mainloop()