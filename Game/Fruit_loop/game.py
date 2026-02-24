from .grid import Grid
from .player import Player
from . import pickups

player = Player(2,1)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)

def print_status(game_grid):
    print("----------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

command = "a"

while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d" and player.can_move(1,0, g):
        maybe_item = g.get(player.pos_x +1, player.pos_y)
        player.move(1,0)

        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points. ")
            g.clear(player.pos_x, player.pos_y)

print("Thank you for playing!")
