import random
class Item:
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("pear"), Item("Strawberry"), Item("Cherry"), Item("watermelon"), Item("banana"), Item("apple"),
           Item("Orange")]

def randomize(grid):
    # 1. Place half the items specifically in "Room zones"
    # Let's target the Top Left Room (x: 4-7, y: 3-6)
    room_items = pickups[:3] # First 3 fruits
    other_items = pickups[3:] # Remaining fruits

    for item in room_items:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            # Randomize within the boundaries of the Top-Left room
            x = random.randint(4, 7)
            y = random.randint(3, 6)
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                placed = True
            attempts += 1

    # 2. Place the rest of the items anywhere else on the map
    for item in other_items:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            # This check ensures we NEVER overwrite a wall ('■')
            # or a lava trail ('~')
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break
