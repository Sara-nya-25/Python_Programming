import random
class Item:
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def __repr__(self):  # Add this for better debugging
        return self.symbol

pickups = [Item("pear"), Item("Strawberry"), Item("Cherry"), Item("watermelon"), Item("banana"), Item("apple"),
           Item("Orange")]

def randomize(grid):
    # 1. Place half the items specifically in "Room zones"
    # Let's target the Top Left Room (x: 4-7, y: 3-6)
    room1_fruits = pickups[0:2] # First 2 fruits
    room2_fruits = [pickups[2]]    # Third fruit
    remaining_fruits = pickups[3:] # Remaining fruits

    # 2. Helper to place items in a specific area
    def place_in_zone(items, x1, x2, y1, y2):
        for fruit in items:
            placed = False
            attempts = 0
            while not placed and attempts < 50:
                a = random.randint(x1, x2)
                b = random.randint(y1, y2)
                if grid.is_empty(a, b):
                    grid.set(a, b, fruit)
                    placed = True
                attempts += 1

    # Place 2 fruits in Room 1 (Top Left: 4-7, 3-6)
    place_in_zone(room1_fruits, 4, 7, 3, 6)

    # Place 1 fruit in Room 2 (Bottom Right based on your previous Grid logic)
    # Boundaries: x = width-9 to width-5, y = height-6 to height-4
    r2_x1, r2_x2 = grid.width - 9, grid.width - 5
    r2_y1, r2_y2 = grid.height - 6, grid.height - 4
    place_in_zone(room2_fruits, r2_x1, r2_x2, r2_y1, r2_y2)

    # 3. Place the rest of the items randomly anywhere else
    for item in remaining_fruits:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()

            # Check if x and y are NOT inside Room 1
            in_room1 = (4 <= x <= 7) and (3 <= y <= 6)

            # Check if x and y are NOT inside Room 2
            r2_x1, r2_x2 = grid.width - 9, grid.width - 5
            r2_y1, r2_y2 = grid.height - 6, grid.height - 4
            in_room2 = (r2_x1 <= x <= r2_x2) and (r2_y1 <= y <= r2_y2)

            # Only place if it's empty AND not in either room
            if grid.is_empty(x, y) and not in_room1 and not in_room2:
                grid.set(x, y, item)
                break


def spawn_single_fruit(grid):
    fruit_names = ["Pear", "Strawberry", "Cherry", "Watermelon", "Banana", "Apple", "Orange"]
    new_fruit = Item(random.choice(fruit_names))

    # Try to find a random empty spot
    for _ in range(100):  # Limit attempts to prevent infinite loops if grid is full
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, new_fruit)
            return True
    return False