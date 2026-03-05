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
g.place_traps(8)

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
    print("'@' - Player \n'O' - Fruits you pickup\n'~' - Lava trail\n'X' - Trap")
    print("For every step on TRAP 'X' -10 points")
    print("For every MOVE -1 point and you leave ONE '~' lava trail ")
    print("For every Step into LAVA '~' -5 points")
    print("Press 'p' to see your pickups")
    print("Use Keys 'w'- Move up, 's'- Move down, 'a'- Move left, 'd'- Move right")
    print("Press 'q' or 'x' to quit.")
    print(f"You are given {score} points initially.")

print_instructions()
active_bombs = []

def print_status(game_grid):
    print("--------FRUIT LOOPS GAME---------")
    print(f"Your Score {score} points.")
    if grace_steps > 0:
        print(f"🛡️ GRACE PERIOD: {grace_steps} steps of protection left!")
    #print(game_grid)
    print(game_grid.__str__(active_bombs))
    if active_bombs:
        for b in active_bombs:
            print(f"💣 Bomb at ({b[0]}, {b[1]}) exploding in {b[2]} moves!")

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
    # Handle placing a bomb
    if command == "b":
         # Place bomb at player's current position
        active_bombs.append([player.pos_x, player.pos_y, 3])
        print("💣 BOMB PLACED! Move 3 times to detonate!")
        continue
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

        # TRAP LOGIC
        if tile_content == "X":
            if grace_steps > 0:
                print("🛡️ Grace Period blocked the Trap! (0 points lost)")
            else:
                print("💥 KA-BOOM! You hit a trap! -10 points")
                score -= 10

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
            elif tile_content != 'X' and not item_found:
                if grace_steps == 0:
                    score -= 1  # Regular movement cost
                # 3. Decrease Grace Period after movement
        if grace_steps > 0 and not item_found:
           grace_steps -= 1
        # Before moving, turn the current floor tile into lava
        old_tile = g.get(player.pos_x, player.pos_y)
        if old_tile not in ["X", "E"]:
            g.set(player.pos_x, player.pos_y, "~")

        # Handle items at the new location
        #maybe_item = g.get(new_x, new_y)

        # Update position
        player.pos_x = new_x
        player.pos_y = new_y

        move_count += 1
        """ BOMB logic start"""
        bombs_to_remove = []
        for bomb in active_bombs:
            bomb[2] -= 1  # Countdown fuse

            if bomb[2] <= 0:
                print("\n💥 KABOOM!")
                bx, by, _ = bomb
                # 3x3 Explosion Loop
                for nx in range(bx - 1, bx + 2):
                    for ny in range(by - 1, by + 2):
                        if g.is_in_bounds(nx, ny):
                            # Prevent destroying the very outer edges of the map
                            is_edge = (nx == 0 or nx == g.width - 1 or
                                       ny == 0 or ny == g.height - 1)

                            target = g.get(nx, ny)
                            if not is_edge and target in [g.wall, "X", "~", "O"]:
                                g.set(nx, ny, g.empty)

                            if nx == player.pos_x and ny == player.pos_y:
                                print("🔥 Caught in blast! -15 points")
                                score -= 15
                bombs_to_remove.append(bomb)

        for b in bombs_to_remove:
            active_bombs.remove(b)


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
