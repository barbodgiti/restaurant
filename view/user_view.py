from view.component_tbl import *

menu_list_burger = [(1, "Burger", 198),
                    (2, "Cheese Burger", 228),
                    (3, "Mushroom Burger", 178),
                    (4, "Double Burger", 218),
                    (5, "Double Cheese Burger", 248),
                    (6, "Bacon Burger", 208),
                    (7, "Zinger Burger", 238),
                    (8, "Double Zinger Burger", 258),
                    (9, "Butter Zinger Burger", 268),
                    (10, "Special Burger", 298)]

menu_list_pizza = [(1, "Peperoni", 239),
                   (2, "Garlic And Meat", 269),
                   (3, "Mushroom And Meat", 259),
                   (4, "Chicken And Vej", 249),
                   (5, "Special", 309),
                   (6, "Roast Beef", 429), ]

menu_list_drink = [(1, "Coke", 20),
                   (2, "Mojito", 50),
                   (3, "Water", 7),
                   (4, "ButterMilk", 15),
                   (5, "Bear", 60),
                   (6, "Big Bear", 100),
                   (7, "Lemonade", 20), ]

menu_list_more = [(1, "Fries", 80),
                  (2, "Fries with Cheese", 100),
                  (3, "Special Fries", 140),
                  (4, "Fries With Mushroom", 110),
                  (5, "Salad", 160),
                  (6, "Sizar Salad", 230),
                  (7, "Season Salad", 200),
                  (8, "Bacon And Cheese With Chips", 350), ]


sabad_list =[]


class UserView:
    def __init__(self):
        self.window = Tk()
        self.window.title("RESTAURANT")
        self.window.geometry("900x600")



        def burger_tbl_click(row):
            #burg = print(row)
            sabad_list.append(row)
            #new_burg = Table(self.window, ["Number", "Burger", "Price"], [100, 140, 100], 20,600, burger_tbl_click)

        def pizza_tbl_click(row):
            #piz = print(row)
            sabad_list.append(row)

        def drink_tbl_click(row):
            #dri = print(row)
            sabad_list.append(row)

        def more_tbl_click(row):
            #mro = print(row)
            sabad_list.append(row)

        burger_tbl = Table(self.window, ["Number", "Burger", "Price"], [100, 140, 100], 20, 20, burger_tbl_click)
        pizza_tbl = Table(self.window, ["Number", "Burger", "Price"], [100, 140, 100], 20, 320, pizza_tbl_click)
        drink_tbl = Table(self.window, ["Number", "Drink", "Price"], [100, 140, 100], 530, 320, drink_tbl_click)
        more_tbl = Table(self.window, ["Number", "More", "Price"], [100, 140, 100], 530, 20, more_tbl_click)

        burger_tbl.set_data(menu_list_burger)
        pizza_tbl.set_data(menu_list_pizza)
        drink_tbl.set_data(menu_list_drink)
        more_tbl.set_data(menu_list_more)

        #burger_list = list(filter(lambda p: p["burger"] == "", sabad_list))


        self.window.mainloop()

print(sabad_list)