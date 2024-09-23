import re

class Validation:
    @classmethod
    def name_validate(cls, name, message):
        if re.match(r'^[a-zA-Z\s]{2,20}$', name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def family_validate(cls, family, message):
        if re.match(r"^[\w\s]{2,30}$", family):
            return family
        else:
            raise ValueError(message)


    @classmethod
    def username_validate(cls, username, message):
        if re.match(r"^[\w._\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validate(cls, password, message):
        if re.match(r"^[\w._]{8,12}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def phone_validate(cls, phone, message):
        if re.match(r"^[0-9]{11}$", phone):
            return phone
        else:
            raise ValueError(message)


