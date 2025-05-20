from customer import Customer
from coffee import Coffee
from order import Order

# Clear existing orders just in case (if rerunning)
Order._all_orders.clear()

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")

# Create some coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cold_brew = Coffee("Cold Brew")

# Create orders
alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
charlie.create_order(cold_brew, 6.0)
charlie.create_order(latte, 4.0)

# Inspect orders
print("All Orders:")
for order in Order.all():
    print(f"{order.customer.name} ordered {order.coffee.name} for ${order.price}")

# Customer -> orders & coffees
print("\nAlice's Orders:")
for o in alice.orders():
    print(f"{o.coffee.name} - ${o.price}")

print("\nAlice's Coffees:")
for c in alice.coffees():
    print(c.name)

# Coffee -> orders & customers
print("\nLatte Orders:")
for o in latte.orders():
    print(f"{o.customer.name} paid ${o.price}")

print("\nLatte Customers:")
for cust in latte.customers():
    print(cust.name)

# Coffee aggregates
print(f"\nNumber of Latte Orders: {latte.num_orders()}")
print(f"Average Latte Price: ${latte.average_price():.2f}")

# Bonus: Who's the most aficionado?
aficionado = Customer.most_aficionado(latte)
print(f"\nMost Aficionado for Latte: {aficionado.name if aficionado else 'None'}")
