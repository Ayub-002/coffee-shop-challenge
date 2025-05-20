import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order._all_orders.clear()
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_orders_and_customers(self):
        self.customer.create_order(self.coffee, 4.0)
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertIn(self.customer, self.coffee.customers())

    def test_num_orders_and_average_price(self):
        self.customer.create_order(self.coffee, 4.0)
        self.customer.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertEqual(self.coffee.average_price(), 5.0)
