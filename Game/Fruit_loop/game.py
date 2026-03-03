from grid import Grid
from player import Player
import pickups


score = 30
inventory = []
move_count = 0  # check for moves, after 25 moves new fruit is placed
grace_steps = 0 # after u pickup a fruit, move 5 steps without reducing score
g = Grid()
start_x, start_y = g.get_center()
player = Player(start_x, start_y)
g.set_player(player)
g.make_walls()
g.make_internal_walls() # Creates the new contiguous internal walls
g.place_exit()
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
    if grace_steps > 0:
        print(f"🛡️ GRACE PERIOD: {grace_steps} steps of protection left!")
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
        tile_content = g.get(new_x, new_y)
        item_found = False

        if tile_content == "E":
            if len(inventory) == 7:
                print("\nVICTORY! You reached the exit with all fruits!")
                break
            else:
                print(f"\nThe exit is locked! Collect all fruits first.")
                # Don't move onto the exit tile if it's locked to avoid overwriting it with lava
                continue

        if isinstance(tile_content, pickups.Item):
            score += tile_content.value
            inventory.append(tile_content.name)
            grace_steps = 5  # <--- NEW: Grant 5 protected steps
            item_found = True
            print(f"You found a {tile_content.name}, +{tile_content.value} points. ")
            print(f"🛡️ GRACE PERIOD: You get {grace_steps} steps of protection!")
            # g.clear(player.pos_x, player.pos_y)
            g.clear(new_x, new_y)

        # CHECK: Is the place you are going ALREADY lava?
        if tile_content == "~":
            if grace_steps > 0:
                print(f"🛡️ Grace Period blocked the lava damage!")
            else:
                print("Ouch! You are in lava! -5 points") # Stepping on to lava tile '~' costs -5 points
                score -= 5
        else:
            if grace_steps > 0:
                # No points deducted for regular movement during grace period
                print("🛡️ Grace Period: Free move!")
            else:
                score -= 1  # Regular movement cost
                # 3. Decrease Grace Period after movement
        if grace_steps > 0 and not item_found:
           grace_steps -= 1
        # Before moving, turn the current floor tile into lava
        g.set(player.pos_x, player.pos_y, "~")

        # Handle items at the new location
        #maybe_item = g.get(new_x, new_y)

        # Update position
        player.pos_x = new_x
        player.pos_y = new_y

        move_count += 1
        if move_count % 25 == 0:
            if pickups.spawn_single_fruit(g):
                print("\n✨ The soil is fertile! A new fruit has sprouted somewhere! ✨")

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

print("Thank you! Play Again!")
