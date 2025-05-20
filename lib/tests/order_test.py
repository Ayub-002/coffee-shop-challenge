import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order._all_orders.clear()
        self.customer = Customer("Alice")
        self.coffee = Coffee("Mocha")

    def test_order_initialization(self):
        order = Order(self.customer, self.coffee, 5.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.5)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 20.0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Order("not_customer", self.coffee, 5.0)
        with self.assertRaises(TypeError):
            Order(self.customer, "not_coffee", 5.0)

    def test_all_orders_classmethod(self):
        Order(self.customer, self.coffee, 5.0)
        self.assertEqual(len(Order.all()), 1)
