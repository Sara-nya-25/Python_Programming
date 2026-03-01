from grid import Grid
from player import Player
import pickups


score = 30
inventory = []

g = Grid()
start_x, start_y = g.get_center()
player = Player(start_x, start_y)
g.set_player(player)
g.make_walls()
g.make_internal_walls() # Creates the new contiguous internal walls
pickups.randomize(g)

# A dictionary to map keys to (dx, dy) movements
moves = {
    "w": (0, -1), # Up
    "s": (0, 1),  # Down
    "a": (-1, 0), # Left
    "d": (1, 0)   # Right
}
print("--------FRUIT LOOPS GAME START---------")
def print_instructions():
    print("********** Instructions **********")
    print("'@' - player \n'?' - Fruits you pickup\n'~' - lava trail")
    print(f"You are given {score} points initially.")
    print("For every move -1 point, you leave one '~' lava trail ")
    print("For every Step into lava '~' -5 points")
    print("Press 'p' to see your pickups")
    print("Use Keys 'w'- Move up, 's'- Move down, 'a'- Move left, 'd'- Move right")

print_instructions()

def print_status(game_grid):
    print("--------FRUIT LOOPS GAME---------")
    print(f"Your Score {score} points.")
    print(game_grid)

command = "a"

while command not in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    # Handle Quit
    if command in ["q", "x"]:
        break  # Exit the loop right away without running movement code
    # Display Instructions 'i'
    if command == 'i':
        print_instructions()
        continue
    # Handle the pickup list
    if command == "p":
        if not inventory:
            print("\nYour inventory is empty.")
        else:
            print("\n--- Pickup List ---")
            for item in inventory:
                print(f"- {item}")
        input("\nPress Enter to continue...")
        continue  # Skip the movement logic for this turn

    dx, dy = 0, 0
    if command in moves:
        dx, dy = moves[command]

    if player.can_move(dx, dy, g):

        new_x = player.pos_x + dx
        new_y = player.pos_y + dy

        # CHECK: Is the place you are going ALREADY lava?
        if g.get(new_x, new_y) == "~":
            print("Ouch! You are in lava! -5 points") # Stepping on to lava tile '~' costs -5 points
            score -= 5
        else:
            score -= 1  # Regular movement costs -1

        # Before moving, turn the current floor tile into lava
        g.set(player.pos_x, player.pos_y, "~")

        # Handle items at the new location
        maybe_item = g.get(new_x, new_y)
        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points. ")
            #g.clear(player.pos_x, player.pos_y)
            g.clear(new_x, new_y)

            # Update position
        player.pos_x = new_x
        player.pos_y = new_y
    elif command in moves:
        # This triggers only if the command was a move but can_move returned False
        print("\nOOPS! You bumped into a wall!")
        score -= 2  # Optional: penalty for bumping into walls

    if score < 0:
        print("\nGAME OVER: You stayed in the lava too long!")
        break
    #player.move(dx, dy, g)
if score > 80:
    print("\nBrilliant! You are a Star Player ⭐⭐⭐!" )
    print("You Won a Gold Trophy 🏆")
elif 50 < score < 80:
    print("\nExcellent! You are Amazing!")
    print("You Won a Silver 🥈")
elif 30 < score < 50:
    print("Good Playing!")
    print("You won a Bronze medal 🥉")
print("Thank you for playing!")
