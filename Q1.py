class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Email: {self.email}")


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")  # Display price with 2 decimal places
        print(f"Description: {self.description}")


class Order(Customer, Product):  # Multiple Inheritance
    def __init__(self, customer_name, customer_email, product_name, price, description, order_id, quantity):
        Product.__init__(self, product_name, price, description)  # Corrected parameter order
        Customer.__init__(self, customer_name, customer_email)
        self.order_id = order_id
        self.quantity = quantity

    def calculate_total(self):
        # Corrected calculation
        return self.price * self.quantity

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        self.display_info()
        print(f"Quantity: {self.quantity}")
        print(f"Total Amount: ${self.calculate_total():.2f}")  # Display total with 2 decimal places


# Create an order
order = Order("Alice", "alice@example.com", "Smartphone", 499.99, "High-end smartphone", "ORD123", 2)

# Display order details
order.display_order()
