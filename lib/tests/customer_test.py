import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order._all_orders.clear()  # Reset orders
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 20)

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertIsInstance(order, Order)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)

    def test_orders_and_coffees(self):
        c2 = Coffee("Espresso")
        self.customer.create_order(self.coffee, 3.5)
        self.customer.create_order(c2, 4.0)
        self.assertEqual(len(self.customer.orders()), 2)
        self.assertIn(self.coffee, self.customer.coffees())
        self.assertIn(c2, self.customer.coffees())

    def test_most_aficionado(self):
        bob = Customer("Bob")
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 3.0)
        bob.create_order(self.coffee, 7.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), self.customer)
