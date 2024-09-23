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
    def edit(cls, id, name, family, username, password, phone):
        try:
            user = User(id, name, family, username, password, phone)
            cls.User_da.edit(user)
            return True, f"User {username} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, username):
        try:
            cls.User_da.remove(username)
            return True, f"User {username} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            return True, cls.User_da.find_by_username_and_password(username, password)
        except Exception as e:
            return False, str(e)

    @classmethod
    def online_book(cls, username):
        try:
            cls.User_da.online_book(username)
            return True, f"User {username} Online Booking"
        except Exception as e:
            return False, str(e)

    @classmethod
    def ofline_book(cls, username):
        try:
            cls.User_da.ofline_book(username)
            return True, f"User {username} Ofline Booking"
        except Exception as e:
            return False, str(e)
