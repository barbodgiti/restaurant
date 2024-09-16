from view.component_tbl import *

class MenuItem:
    def __init__(self, id, name, food_type, price, description):
        self.id = id
        self.name = name
        self.food_type = food_type
        self.price = price
        self.description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def food_type(self):
        return self._food_type

    @food_type.setter
    def food_type(self, food_type):
        self._food_type = food_type

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description



menu_list_burger = [(1,"Burger",198),
             (2,"Cheese Burger",228),
             (3,"Mushroom Burger",178),
             (4,"Double Burger",218),
             (5,"Double Cheese Burger",248),
             (6,"Bacon Burger",208),
             (7,"Zinger Burger",238),
             (8,"Double Zinger Burger",258),
             (9,"Butter Zinger Burger",268),
             (10,"Special Burger",298)]

menu_list_pizza = [(1,"Peperoni",239),
                   (2,"Garlic And Meat",269),
                   (3,"Mushroom And Meat",259),
                   (4,"Chicken And Vej",249),
                   (5,"Special",309),
                   (6,"Roast Beef",429),]

menu_list_drink = [(1,"Coke",20),
                   (2,"Mojito",50),
                   (3,"Water",7),
                   (4,"ButterMilk",15),
                   (5,"Bear",60),
                   (6,"Big Bear",100),
                   (7,"Lemonade",20),]

menu_list_more = [(1,"Fries",80),
                  (2,"Fries with Cheese",100),
                  (3,"Special Fries",140),
                  (4,"Fries With Mushroom",110),
                  (5,"Salad",160),
                  (6,"Sizar Salad",230),
                  (7,"Season Salad",200),
                  (8,"Bacon And Cheese With Chips",350),]


def burger_clc(row):
    print(row)


def pizza_clc(row):
    print(row)


def more_clc(row):
    print(row)


def drink_clc(row):
    print(row)


window = Tk()
window.title("RESTAURANT")
window.geometry("900x600")
window.config(bg="cadetblue1")


burger_tbl = Table(window, ["Number","BURGER","Price"], [100,200,70], 20,10, burger_clc)
pizza_tbl = Table(window, ["Number","PIZZA","Price"], [100,200,70], 20,300, pizza_clc)
more_tbl = Table(window, ["Number","MORE","Price"], [100,200,70], 500,10, more_clc)
drink_tbl = Table(window, ["Number","DRINK","Price"], [100,200,70], 500,300, drink_clc)

burger_tbl.set_data(menu_list_burger)
pizza_tbl.set_data(menu_list_pizza)
more_tbl.set_data(menu_list_more)
drink_tbl.set_data(menu_list_drink)



window.mainloop()