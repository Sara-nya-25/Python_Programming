import csv
import os
from config import FILE_NAME, HEADERS, TABLE_WIDTH
from Product import Product
from init import initialize_inventory_file
# Imports tools from other files and co-ordinates the flow Initialize->Load->Display
def load_products_from_csv(filename):
    products = []
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return products

    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(Product(
                row["product_id"],
                row["product_name"],
                row["price"],
                row["quantity"]
            ))
    return products

def display_inventory(products):
    table_format = "{:<12} {:<25} {:>10} {:>10}"

    print("=" * TABLE_WIDTH)
    print(table_format.format("ID", "PRODUCT NAME", "PRICE", "STOCK"))
    print("-" * TABLE_WIDTH)

    for p in products:
        print(table_format.format(
            p.get_id(),
            p.name,
            f"${p.price:,.2f}",
            p.quantity
        ))

    print("=" * TABLE_WIDTH)


if __name__ == "__main__":
    # Step 1: Initialize (Create file)
    initialize_inventory_file(FILE_NAME, HEADERS)

    # Step 2: Load (Read file into objects)
    inventory = load_products_from_csv(FILE_NAME)

    # Step 3: Use (Display the data)
    display_inventory(inventory)