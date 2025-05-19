# Coffee Shop Challenge

## Project Overview

This project simulates a coffee shop environment with three core models: `Customer`, `Coffee`, and `Order`. The project implements basic object-oriented design principles and allows for managing customers, orders, and coffee products. It includes key functionality such as:

- Customer ordering coffee.
- Tracking orders and prices.
- Aggregating and querying data for each customer and coffee.

## Models

### 1. **Customer**
- **Attributes:**
  - `name` (str): The name of the customer (1–15 characters).
- **Methods:**
  - `.orders()`: Returns a list of orders made by the customer.
  - `.coffees()`: Returns a list of unique coffees ordered by the customer.
  - `.create_order(coffee, price)`: Creates a new order for the customer.
  - `.most_aficionado(coffee)`: Class method that returns the customer who spent the most on a given coffee.

### 2. **Coffee**
- **Attributes:**
  - `name` (str): The name of the coffee (at least 3 characters).
- **Methods:**
  - `.orders()`: Returns a list of orders containing the coffee.
  - `.customers()`: Returns a list of unique customers who have ordered the coffee.
  - `.num_orders()`: Returns the total number of orders for the coffee.
  - `.average_price()`: Returns the average price of orders for the coffee.

### 3. **Order**
- **Attributes:**
  - `customer`: A `Customer` instance.
  - `coffee`: A `Coffee` instance.
  - `price`: A float representing the price of the order (between 1.0 and 10.0).
- **Methods:**
  - Accessors for `customer`, `coffee`, and `price`.
  
## Requirements

- Python 3.10 (or compatible version)
- `pipenv` (for dependency management)

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:<your-username>/coffee-shop-challenge.git
   cd coffee-shop-challenge
