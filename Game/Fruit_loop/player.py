
from Fruit_loop.pickups import pickups
class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 30
        self.inventory = []

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

    def jump(self, dx, dy, grid):
        """
        Version 2 Requirement: Jump (J + WASD).
        Moves two squares in the given direction.
        """
        # Calculate landing coordinates (2 steps away)
        target_x = self.pos_x + (dx * 2)
        target_y = self.pos_y + (dy * 2)

        # Use your existing is_in_bounds and check if the landing spot is clear
        if grid.is_in_bounds(target_x, target_y):
            target_tile = grid.get(target_x, target_y)
            if target_tile != grid.wall:
                self.pos_x = target_x
                self.pos_y = target_y
                return True

        return False  # Jump failed (landing spot is a wall or out of bounds)