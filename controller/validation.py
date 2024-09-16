import re

class Validation:
    @classmethod
    def name_validate(cls, name):
        if re.match(r'^[a-zA-Z\s]{2,20}$', name):
            return name
        else:
            raise ValueError("Invalid Name")