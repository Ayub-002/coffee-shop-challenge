from lib.order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from lib.order import Order
        from lib.coffee import Coffee

        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be a Coffee instance.")

        spending = {}

        for order in Order.all():
            if order.coffee == coffee:
                cust = order.customer
                spending[cust] = spending.get(cust, 0) + order.price

        if not spending:
            return None

        return max(spending, key=spending.get)
