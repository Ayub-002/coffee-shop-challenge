from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 4.0)
c2.create_order(coffee1, 5.0)

print("Orders for Latte:", coffee1.orders())
print("Average price for Latte:", coffee1.average_price())
