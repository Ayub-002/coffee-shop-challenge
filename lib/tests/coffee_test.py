from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_coffee_name_getter():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_validation():
    try:
        Coffee("A")
        assert False
    except ValueError:
        assert True

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    Order(c1, coffee, 3.5)
    Order(c2, coffee, 4.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {c1, c2}

def test_coffee_num_orders_and_average_price():
    coffee = Coffee("Americano")
    c = Customer("Sam")
    Order(c, coffee, 3.0)
    Order(c, coffee, 5.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0
