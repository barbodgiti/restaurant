class Person:
    def __init__(self,name,family):
        self.name = name
        self.family = family

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


    # getter/setter