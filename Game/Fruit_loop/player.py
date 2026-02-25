class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        """Checks if the intended next tile is a wall or out of bounds."""
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        # prevent moving out of grid boundaries
        if not (0 <= new_x < grid.width and 0 <= new_y < grid.height):
            return False
        # prevent walking through the wall
        if grid.get(new_x, new_y) == grid.wall:
            return False
        return True

