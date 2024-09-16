import mysql.connector

from model.entity.user import *


class user_da:

    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='mft'
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, user):
        self.connect()
        self.cursor.execute("INSERT INTO user_tbl (name,family,username,password,food,drink,more,bookingon) VALUES ("
                            "%s,%s,%s,%s,%s,%s,%s,%s)",
                            [user.name, user.family, user.username, user.password, user.food, user.drink, user.more,
                             user.bookingon])
        self.connection.commit()
        self.disconnect()

    def edit(self, user):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET password=%s,food=%s,drink=%s,more=%s,bookingon=%s WHERE username=%s",
                            [user.name, user.family, user.password, user.food, user.drink, user.more, user.bookingon])
        self.connection.commit()
        self.disconnect()

    def remove(self, username):
        self.connect()
        self.cursor.execute("DELETE FROM user_tbl WHERE username=%s", [username])
        self.connection.commit()
        self.disconnect()

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM user_tbl WHERE username=%s and password=%s",
                            [username, password])
        user_tuple = self.cursor.fetchone()
        user = User(*user_tuple)
        self.disconnect()
        return user

    def online_book(self, username):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET bookingon=1 WHERE username=%s", [username])
        self.disconnect()

    def ofline_book(self, username):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET bookingon=0 WHERE username=%s", [username])
        self.disconnect()
