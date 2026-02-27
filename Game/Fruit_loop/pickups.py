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
    for item in pickups:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x,y, item)
                break