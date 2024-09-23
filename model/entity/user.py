# id, name, family, username, password, phone
from controller.validation import *

class User:
    def __init__(self, id, name, family, username, password, phone):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone = phone

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
        self._name = Validation.name_validate(name, "Invalid Name")
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validate(family, "Invalid Family")

    @property
    def username(self):
       return self._username

    @username.setter
    def username(self, username):
        self._username = Validation.username_validate(username, "Invalid Username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validation.password_validate()(password, "Invalid Password")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = Validation.phone_validate(phone, "Invalid Phone")


    def __repr__(self):
        return f"{self.__dict__}
