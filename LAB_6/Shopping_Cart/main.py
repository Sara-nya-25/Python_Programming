import sys
from shopping_cart import ShoppingCart, Order
from load_data import display_inventory, load_products_from_csv
from config import FILE_NAME, HEADERS, TABLE_WIDTH


def find_product_by_name(inventory, search_name):
    #Searches for a product by name (case-insensitive)
    search_name = search_name.strip().lower()
    for p in inventory:
        if search_name in p.name.lower():
            return p
    return None


def shopping_simulation(inventory):
    cart = ShoppingCart()

    print("\n--- WELCOME TO THE PYTHON GROCERY STORE ---")

    while True:
        display_inventory(inventory)
        print("\nOptions: [Product Name] to add to cart | 'checkout' to finish | 'exit' to quit")
        user_input = input("Selection: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()

        elif user_input.lower() == 'checkout':
            if not cart.items:
                print("Your cart is empty!")
            else:
                order = Order(cart)
                order.print_receipt()
                cart.clear_cart()
                print("Thank you for shopping with us!")
                break  # End the simulation after checkout

        else:
            # Try to find the product
            product = find_product_by_name(inventory, user_input)
            if product:
                try:
                    qty = int(input(f"How many {product.name} would you like? "))
                    cart.add_item(product, qty)
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")
            else:
                print(f"{user_input} not found. Check spelling & Please try again.")


# --- Execution ---
if __name__ == "__main__":
    # 1. Load data
    inventory = load_products_from_csv(FILE_NAME)

    # 2. Start the interactive loop
    shopping_simulation(inventory)

    # 3. Final Step: Save the updated stock back to CSV
    # (Optional: You can write a function to save the inventory list back to CSV)