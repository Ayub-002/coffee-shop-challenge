from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_order_initialization():
    c = Customer("Joe")
    coffee = Coffee("Macchiato")
    o = Order(c, coffee, 4.5)

    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 4.5

def test_order_invalid_price():
    c = Customer("Sam")
    coffee = Coffee("Flat White")
    try:
        Order(c, coffee, 0.5)
        assert False
    except ValueError:
        assert True

    try:
        Order(c, coffee, 11.0)
        assert False
    except ValueError:
        assert True

def test_order_static_all():
    Order._all = []  # reset
    c = Customer("Jess")
    coffee = Coffee("Ristretto")
    o1 = Order(c, coffee, 3.0)
    o2 = Order(c, coffee, 4.0)
    assert Order.all() == [o1, o2]
