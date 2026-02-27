from grid import Grid
from player import Player
import pickups


score = 100
inventory = []

g = Grid()
start_x, start_y = g.get_center()
player = Player(start_x, start_y)
g.set_player(player)
g.make_walls()
pickups.randomize(g)

# A dictionary to map keys to (dx, dy) movements
moves = {
    "w": (0, -1), # Up
    "s": (0, 1),  # Down
    "a": (-1, 0), # Left
    "d": (1, 0)   # Right
}

def print_status(game_grid):
    print("----------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

command = "a"

while command not in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    # Handle the new Inventory command
    if command == "i":
        if not inventory:
            print("\nYour inventory is empty.")
        else:
            print("\n--- Inventory ---")
            for item in inventory:
                print(f"- {item}")
        input("\nPress Enter to continue...")
        continue  # Skip the movement logic for this turn

    dx, dy = 0, 0
    if command in moves:
        dx, dy = moves[command]

    if player.can_move(dx, dy, g):
        # Before moving, turn the current floor tile into lava
        g.set(player.pos_x, player.pos_y, "~")
        # The floor is lava! Subtract 1 point for the attempt to move

        new_x = player.pos_x + dx
        new_y = player.pos_y + dy
        # CHECK: Is the place you are going ALREADY lava?
        if g.get(new_x, new_y) == "~":
            print("Ouch! This floor is already melted! -5 points")
            score -= 5
        else:
            score -= 1  # Regular lava cost

        maybe_item = g.get(new_x, new_y)

    #if command == "d" and player.can_move(1,0, g):
     #   maybe_item = g.get(player.pos_x +1, player.pos_y)
      #  player.move(1,0)

        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points. ")
            #g.clear(player.pos_x, player.pos_y)
            g.clear(new_x, new_y)

            # Update position
        player.pos_x = new_x
        player.pos_y = new_y
    if score < 0:
        print("\nGAME OVER: You stayed in the lava too long!")
        break
    #player.move(dx, dy, g)
print("Thank you for playing!")
