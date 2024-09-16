
# id, customer, menu_item, date_time, status, payment
class Order:
    def __init__(self, id, customer, menu_item, date_time, status, payment):
        self.id = id
        self.customer = customer
        self.menu_item = menu_item
        self.date_time = date_time
        self.status = status
        self.payment = payment

    @property
    def id(self):
         return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @property
    def menu_item(self):
        return self._menu_item

    @menu_item.setter
    def menu_item(self, menu_item):
        self._menu_item = menu_item

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        self._payment = payment


    def __repr__(self):
        return f"{self.__dict__}"