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
from .class_4_Product import Product

class ShoppingCart():
    def __init__(self):
        super().__init__("ShoppingCart.csv")
        self.__items = []  # List of Product objects

    def add_product(self, product):
        self.__items.append(product)
        print(f"Added {product.name} to cart.")

    def get_total(self):
        return sum(item.price for item in self.__items)

    def get_items(self):
        return self.__items

    def clear(self):
        self.__items = []

class Order:
    def __init__(self, order_id, cart):
        self.__id = order_id
        # Copying items from cart to order
        self.__ordered_items = list(cart.get_items())
        self.__total = cart.get_total()
        cart.clear() # Cart is emptied after ordering

    def show_order_details(self):
        print(f"\n--- Order Receipt: {self.__id} ---")
        for item in self.__ordered_items:
            print(f"ID: {item.get_id()} | {item.name:.<20} ${item.price:>7.2f}")
        print(f"TOTAL: ${self.__total:>24.2f}\n")

