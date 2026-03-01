import random

class Grid:
    width = 36
    height = 12
    empty = "."
    wall = "■"
    #symbols = ["🟩","■","■"]

    def __init__(self):
        self.data = [[self.empty for y in range(self.width)] for z in range(self.height)]


    def get(self, x, y):
        return self.data[y][x]

    def set(self, x, y, value):
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def get_center(self):
        """Returns the (x, y) coordinates for the center of the grid."""
        center_x = self.width // 2
        center_y = self.height // 2
        return center_x, center_y

    def clear(self, x,y):
        self.set(x, y, self.empty)

    def __str__(self):

        xs = ""
        for y in range(len(self.data)):
            row= self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs

    def make_walls(self):
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width -1, i, self.wall)

        for j in range(1, self.width -1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    def get_random_x(self):
        return random.randint(0, self.width-1)

    def get_random_y(self):
        return random.randint(0, self.height-1)

    def is_empty(self, x, y):
        return self.get(x,y) == self.empty

    def make_internal_walls(self):
        """Creates contiguous segments of walls using for-loops."""
        # 1. Create a vertical divider with a gap in the middle
        # This uses a for loop to create a contiguous line
        mid_x = self.width // 4
        for y in range(2, self.height - 2):
            if y != self.height // 2:  # Leave a gap so it's not a dead end
                self.set(mid_x, y, self.wall)

        # 2. Create a horizontal shelf
        # This uses a for loop to create a contiguous horizontal line
        shelf_y = 3
        for x in range(self.width // 2, self.width - 5):
            # Only set if it's currently empty to avoid blocking the outer border
            if self.is_empty(x, shelf_y):
                self.set(x, shelf_y, self.wall)

        # 3. Create a 'L' shape wall in the bottom right
        for y in range(self.height - 5, self.height - 2):
            self.set(self.width - 8, y, self.wall)
        for x in range(self.width - 8, self.width - 2):
            self.set(x, self.height - 5, self.wall)