
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
        """Creates square rooms with doorways using for-loops."""

        # Room 1: Top Left Room (approx 5x5)
        # We define the boundaries
        top, bottom = 2, 5
        left, right = 4, 9
        gap_y = 4  # The 'door' will be on the right wall at this Y coordinate

        for y in range(top, bottom + 1):
            for x in range(left, right + 1):
                # Only place a wall if it's on the edge of our square
                if x == left or x == right or y == top or y == bottom:
                    # Create a doorway on the right wall
                    if not (x == right and y == gap_y):
                        self.set(x, y, self.wall)

        # Room 2: Bottom Right Room
        # Using a single loop approach for horizontal and vertical lines
        r2_top, r2_bottom = self.height - 7, self.height - 4
        r2_left, r2_right = self.width - 10, self.width - 5
        gap_x = r2_left + 2  # The 'door' will be on the top wall at this X coordinate

        for x in range(r2_left, r2_right + 1):
            if x != gap_x:
                self.set(x, r2_top, self.wall)  # Top wall
            self.set(x, r2_bottom, self.wall)  # Bottom wall

        for y in range(r2_top, r2_bottom + 1):
            self.set(r2_left, y, self.wall)  # Left wall
            self.set(r2_right, y, self.wall)  # Right wall

    def place_exit(self):
        """Places 'E' in a random available corner of the grid."""
        # Define the 4 corners: (0,0), (max_x, 0), (0, max_y), (max_x, max_y)
        # We use +1 or -1 to stay inside the boundary walls if necessary
        corners = [
            (1, 1),  # Top-Left
            (self.width - 2, 1),  # Top-Right
            (1, self.height - 2),  # Bottom-Left
            (self.width - 2, self.height - 2)  # Bottom-Right
        ]

        random.shuffle(corners)  # Mix them up

        for x, y in corners:
            if self.is_empty(x, y):
                self.set(x, y, "E")
                return  # Exit found a home, stop looking

    def place_traps(self, count=5):
        """Places traps 'X' only on empty floor tiles."""
        placed = 0
        # We use a loop to keep trying until we successfully place 'count' traps
        while placed < count:
            x = self.get_random_x()
            y = self.get_random_y()

            # This ensures we don't overwrite walls (■), fruits (?),
            # the exit (E), or the player's current spot (@)
            if self.is_empty(x, y):
                # Double check to make sure we aren't exactly on the player
                if x != self.player.pos_x or y != self.player.pos_y:
                    self.set(x, y, "X")
                    placed += 1