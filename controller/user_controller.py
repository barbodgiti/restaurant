from model.da.user_da import *
from tools.decorators import exception_handling


class UserController:
    User_da = UserDa()

    @classmethod
    @exception_handling
    def save(cls, name, family, username, password, phone):
        user = User(0, name, family, username, password, phone)
        cls.User_da.save(user)
        return True, f"User {username} Saved"

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, username, password, phone):
            user = User(id, name, family, username, password, phone)
            cls.User_da.edit(user)
            return True, f"User {username} Edited"

    @classmethod
    @exception_handling
    def remove(cls, username):
            cls.User_da.remove(username)
            return True, f"User {username} Removed"

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
            return True, cls.User_da.find_by_username_and_password(username, password)

    @classmethod
    @exception_handling
    def online_book(cls, username):
            cls.User_da.online_book(username)
            return True, f"User {username} Online Booking"

    @classmethod
    @exception_handling
    def ofline_book(cls, username):
            cls.User_da.ofline_book(username)
            return True, f"User {username} Ofline Booking"
