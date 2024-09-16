class User:
    def __init__(self, name, family, username, password, food, drink, more, bookingon=True):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.food = food
        self.drink = drink
        self.more = more
        self.bookingon = bookingon

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = family

    @property
    def username(self):
       return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, food):
        self._food = food

    @property
    def drink(self):
        return self._drink

    @drink.setter
    def drink(self, drink):
        self._drink = drink

    @property
    def more(self):
        return self._more

    @more.setter
    def more(self, more):
        self._more = more

    @property
    def bookingon(self):
        return self._bookingon

    @bookingon.setter
    def bookingon(self, bookingon):
        self._bookingon = bookingon

    def __str__(self):
        return f"{self.__dict__}"
