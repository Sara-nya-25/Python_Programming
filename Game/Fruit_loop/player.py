from grid import Grid

class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 0

    def move(self, dx, dy, grid):
        # Adjust move only if path is clear
        if self.can_move(dx, dy, grid):
            self.pos_x += dx
            self.pos_y += dy

        current_tile = grid.get(self.pos_x, self.pos_y)
        if current_tile == "S":  # Fruit Salad
            self.score += 20
            grid.clear(self.pos_x, self.pos_y)
        elif current_tile == "o":  # Standard Fruit
            self.score += 10
            grid.clear(self.pos_x, self.pos_y)
        else:
            # Optional: feedback for hitting a wall
            pass


    def can_move(self, dx, dy, grid):
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

