"""
Create classes that represent a webshop:
Products (Product)
Orders (Order)
ShoppingCart (ShoppingCart)
Tip 1! Give each class a property "__id". You can use it to refer to another object.
This is needed because both shopping cart and orders will contain existing products.
Tip 2! You can use AI to create realistic test data. Try starting with:
"Create test data for 10 products for a webshop, which sells tools. Display the data in a table.
Each product should have a name, price and a unique id."
"""
from Product import Product
import datetime
class ShoppingCart():
    def __init__(self):
       self.items = []  # List of Product objects

    def add_item(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append((product, quantity))
            # Reduce stock in the master inventory
            product.quantity -= quantity
            print(f"Added {quantity}x {product.name} to cart.")
        else:
            print(f"Sorry, only {product.quantity} units of {product.name} available.")

    def calculate_total(self):
        return sum(item[0].price * item[1] for item in self.items)

    def clear_cart(self):
        self.items = []

    def get_items(self):
        return self.items


class Order:
    def __init__(self, cart):
        self.order_id = f"ORD-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.order_items = list(cart.items)
        self.total_amount = cart.calculate_total()
        self.timestamp = datetime.datetime.now()

    def print_receipt(self):
        print("\n" + "*" * 40)
        print(f"RECEIPT - {self.order_id}")
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print("-" * 40)

        for product, qty in self.order_items:
            subtotal = product.price * qty
            print(f"{product.name:<25} {qty:>2} x ${product.price:>7.2f} = ${subtotal:>8.2f}")

        print("-" * 40)
        print(f"{'TOTAL:':<30} ${self.total_amount:>9.2f}")
        print("*" * 40 + "\n")
