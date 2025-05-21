from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_customer_name_setter_getter():
    c = Customer("Amy")
    assert c.name == "Amy"
    c.name = "John"
    assert c.name == "John"

def test_customer_name_validation():
    try:
        Customer("")
        assert False
    except ValueError:
        assert True

    try:
        Customer("A" * 16)
        assert False
    except ValueError:
        assert True

def test_customer_create_order():
    c = Customer("Zoe")
    coffee = Coffee("Mocha")
    c.create_order(coffee, 5.0)
    assert len(c.orders()) == 1
    assert c.orders()[0].coffee == coffee

def test_customer_coffees_unique():
    c = Customer("Tom")
    coffee = Coffee("Latte")
    c.create_order(coffee, 3.0)
    c.create_order(coffee, 4.0)
    assert c.coffees() == [coffee]
