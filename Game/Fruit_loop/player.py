
from Fruit_loop.pickups import pickups
class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 100
        self.inventory = []

    def move(self, dx, dy, grid):
        # Adjust move only if path is clear
        if self.can_move(dx, dy, grid):
            self.pos_x += dx
            self.pos_y += dy
            self.score -= 1
            current_tile = grid.get(self.pos_x, self.pos_y)
            # Check if the tile contains an Item object

            if isinstance(current_tile, Item):
                # If Fruit,u pickup item worth 20 points
                self.score += current_tile.value
                self.inventory.append(current_tile.name)
                print(f"Picked up: {current_tile.name} (+{current_tile.value} pts)")
                grid.clear(self.pos_x, self.pos_y)

        else:
            # Feedback for hitting a wall
            print("BONK! (Still standing in lava, -1 point)")
            self.score -= 1

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
        # Calculate landing spot (2 steps away)
        jump_x, jump_y = dx * 2, dy * 2

        # If the jump destination is valid, move there
        if self.can_move(jump_x, jump_y, grid):
            self.pos_x += jump_x
            self.pos_y += jump_y
            return True

        # If jumping into a wall, Version 2 says it's like a normal step
        elif self.can_move(dx, dy, grid):
            self.pos_x += dx
            self.pos_y += dy
            return True

        return False