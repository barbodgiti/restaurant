import mysql.connector

from model.entity.user import *


class UserDa:

    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='barbod.87.08',
            database='gks'
        )
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, user):
        self.connect()
        self.cursor.execute(
            "INSERT INTO user_tbl (id,name,family,username,password,phone) VALUES (""%s,%s,%s,%s,%s,%s)",
            [user.id, user.name, user.family, user.username, user.password, user.phone])
        self.disconnect(True)

    def edit(self, user):
        self.connect()
        self.cursor.execute("UPDATE user_tbl SET password=%s WHERE username=%s",
                            [user.password])
        self.disconnect(True)

    def remove(self, username):
        self.connect()
        self.cursor.execute("DELETE FROM user_tbl WHERE username=%s", [username])
        self.disconnect(True)

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
