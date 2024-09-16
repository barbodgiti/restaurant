from model.user_da import *



class UserController:

    User_da = user_da()

    @classmethod
    def save(ksi, name, family, username, password, food, drink, more, bookingon):
         try:
             user = User(name, family, username, password, food, drink, more, bookingon)
             ksi.User_da.save(user)
             return True, f"User {username} Saved"
         except Exception as e:
             return False, str(e)


    @classmethod
    def edit(ksi, name, family, username, password, food, drink, more, bookingon):
        try:
            user = User(name, family, username, password, food, drink, more, bookingon)
            ksi.User_da.edit(user)
            return True, f"User {username} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(ksi,username):
        try:
            ksi.User_da.remove(username)
            return True, f"User {username} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_and_password(ksi, username, password):
        try:
            return True, ksi.User_da.find_by_username_and_password(username, password)
        except Exception as e:
            return False, str(e)


    @classmethod
    def online_book(ksi,username):
        try:
            ksi.User_da.online_book(username)
            return True, f"User {username} Online Booking"
        except Exception as e:
            return False, str(e)

    @classmethod
    def ofline_book(ksi,username):
        try:
            ksi.User_da.ofline_book(username)
            return True, f"User {username} Ofline Booking"
        except Exception as e:
            return False, str(e)
