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

