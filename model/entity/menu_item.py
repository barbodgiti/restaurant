# todo : validation
from tools.validator import Validator


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
        self._name = Validator.name_validator(name, "Invalid Name")

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


    def __repr__(self):
        return f"{self.__dict__}"