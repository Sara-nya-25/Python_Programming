import csv

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__id = product_id  # Private ID property
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_id(self):
        return self.__id


def create_csv(filename):
    headers = ["product_id", "product_name", "price", "quantity"]
    data = [
        ["MIL001", "Milk 3%", 26.90, 500],
        ["MIL002", "Milk Eko", 28.90, 300],
        ["MIL003", "Milk 1.5% ", 21.90, 200],
        ["EGG001", "Egg", 48.99, 300],
        ["HCHK88", "Full Chicken", 89.99, 75],
        ["BRCHK99", "Chicken Breast", 119.90, 45],
        ["FRORG01", "Orange", 35.90, 80],
        ["FRPIN01", "Pineapple", 35, 150],
        ["FRBANA1", "Banana Eko", 28.90, 110],
        ["FRAPP02", "Apple Royal Gala", 32.90, 200],
        ["FRGRAP1", "Grapes", 80, 300],
        ["VEGTOM12", "Tomato", 52.90, 125],
        ["VEGCAR14", "Carrot", 20, 300],
        ["VEGCUCU8", "Cucucmber", 15, 400],
        ["VEGONI21", "Onion", 16.90, 500],
        ["VEGGIN3", "Ginger", 69.90, 85],
        ["VEGGARL9", "Garlic", 149.90, 100],
        ["COCOMB11", "Marabou Milk chocolate", 38.90, 550],
        ["COCOFAZ1", "Fazer Coco Nut", 50.90, 400],
        ["COCOMR3", "Marabou Hazelnut", 45.90, 350],
        ["COCOMR4", "Marabou White Cranberry", 52.90, 250]

    ]

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerows(data)
    print(f"{filename} created successfully.")


def load_products(filename):
    product_list = []
    try:
        with open(filename, mode='r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                item = Product(
                    row["product_id"],
                    row["product_name"],
                    row["price"],
                    row["quantity"],
                )
                product_list.append(item)
    except FileNotFoundError:
        print(f"File {filename} not found.")

    return product_list


# Display product list
def display_inventory_table(products):
    # Define headers
    header_id = "ID"
    header_name = "Product Name"
    header_price = "Price"
    header_stock = "Stock"

    # Create a format string for alignment
    # <10: left align, 10 spaces | >10: right align, 10 spaces
    table_format = "{:<8} {:<25} {:>10} {:>10}"

    print("-" * 56)
    print(table_format.format(header_id, header_name, header_price, header_stock))
    print("-" * 56)

    for p in products:
        print(table_format.format(
      p.get_id(),
            p.name,
            f"${p.price:,.2f}",
            p.quantity
        ))

    print("-" * 56)


file_name = 'inventory.csv'
create_csv(file_name)
inventory = load_products(file_name)
display_inventory_table(inventory)