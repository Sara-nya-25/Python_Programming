class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__id = product_id  # Private attribute
        self.name = name
        # Convert to numbers immediately to avoid "format code" errors
        self.price = float(price)
        self.quantity = int(quantity)

    def get_id(self):
        return self.__id