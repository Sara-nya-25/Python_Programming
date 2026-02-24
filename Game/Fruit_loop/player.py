class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        return True

