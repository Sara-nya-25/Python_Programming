from Fruit_loop.grid import Grid
from Fruit_loop.player import Player
import Fruit_loop.pickups as pickups



def print_instructions(score):
    print("********** Instructions **********")
    print("SYMBOLS USED")
    print("'@' - Player \n'O' - Fruits you pickup (+10 points)"
          "\n'~' - Lava trail (-5 points)\n'X' - Trap(-10 points)"
          "\n'K' - Key to open Chest C\n'C' - Chest(+100 points)"
          "\n'j' + Move(wasd), Jump 2 tiles"
          "\n'q' - quit or exit\n'Wrong command'- (-2 points)")
    print("For every MOVE -1 point and you leave ONE '~' lava trail ")
    print("Pick KEY 'K' to open TREASURE CHEST 'C' to grab Surprise points")
    print("Press 'b' to place Bombs 💣, it blasts after 3 moves")
    print("Press 'p' to see fruit list, Press 'h' to see instructions")
    print("Use Keys 'w'- Move up, 's'- Move down, 'a'- Move left, 'd'- Move right")
    print("For every 25 moves, new fruit '?' is placed in the grid")
    print("Press 'q' or 'x' to quit.")
    print(f"You are given {score} points initially.")

def print_status(game_grid, score, grace_steps, active_bombs):
    print("--------FRUIT LOOPS GAME---------")
    print(f"Your Score {score} points.")
    if grace_steps > 0:
        print(f"🛡️ GRACE PERIOD: {grace_steps} steps of protection left!")
    #print(game_grid)
    print(game_grid.__str__(active_bombs))
    if active_bombs:
        for b in active_bombs:
            print(f"💣 Bomb at ({b[0]}, {b[1]}) exploding in {b[2]} moves!")


def handle_explosions(g, active_bombs, player_pos):
    """Processes bomb countdowns and returns total penalty for player."""
    penalty = 0
    bombs_to_remove = []

    for bomb in active_bombs:
        bomb[2] -= 1
        if bomb[2] <= 0:
            print("\n💥 KABOOM!")
            bx, by, _ = bomb
            for nx in range(bx - 1, bx + 2):
                for ny in range(by - 1, by + 2):
                    if g.is_in_bounds(nx, ny):
                        # Don't destroy map borders
                        if not (nx == 0 or nx == g.width - 1 or ny == 0 or ny == g.height - 1):
                            target = g.get(nx, ny)
                            if target in [g.wall, "X", "~", "O"]:
                                g.clear(nx, ny)

                        if (nx, ny) == player_pos:
                            print("🔥 Caught in blast! -15 points")
                            penalty += 15
            bombs_to_remove.append(bomb)

    for b in bombs_to_remove:
        active_bombs.remove(b)
    return penalty

def is_exit_blocked(g, target_x, target_y, inventory):
    """Checks if the target tile is a locked Exit."""
    if g.is_in_bounds(target_x, target_y) and g.get(target_x, target_y) == "E":
        fruit_count = len([i for i in inventory if i != "Key"])
        if fruit_count < 7:
            print(f"\n🔒 EXIT LOCKED! You need 7 fruits (You have {fruit_count}).")
            return True # Yes, it is blocked
    return False # No, it's either not the exit or the exit is open

def play_game():
    score = 30
    inventory = []
    move_count = 0  # check for moves, after 25 moves new fruit is placed
    grace_steps = 0 # after u pickup a fruit, move 5 steps without reducing score
    active_bombs = []
    g = Grid()
    start_x, start_y = g.get_center()
    player = Player(start_x, start_y)
    g.set_player(player)
    g.make_walls()
    g.make_internal_walls() # Creates the new contiguous internal walls
    g.place_exit()
    pickups.randomize(g)
    item_found = False
    tile_content = 0
    new_x, new_y = 0, 0
    g.place_traps(8)
    pickups.place_chests_and_keys(g, 1)
    # A dictionary to map keys to (dx, dy) movements
    moves = {
        "w": (0, -1), # Up
        "s": (0, 1),  # Down
        "a": (-1, 0), # Left
        "d": (1, 0)   # Right
    }



    print("--------FRUIT LOOPS GAME START---------")
    print_instructions(score)

    while score >= 0:
        print_status(g, score, grace_steps, active_bombs)

        command = input("Move (WASD) or Jump j+(WASD),\nBomb(b), Help(h), Quit(Q/X). ").lower().strip()
        cmd = command.casefold()[:1]

        if not command:
            continue
        match cmd:
            case 'q' | 'x' : break
            case 'h':
                print_instructions(score)
                continue
            case 'p':
                print(f"Fruits Picked: {inventory if inventory else 'Fruit List is Empty'}")
                input("Press Enter...")
                continue
            case 'b':
                active_bombs.append([player.pos_x, player.pos_y, 3])
                print("💣 Bomb set!")
                continue

        is_jumping = False
        direction_key = command
        #dx, dy = 0, 0
        if command.startswith('j') and len(command) > 1:
            is_jumping = True
            direction_key = command[1]

        if direction_key in moves:
            dx, dy = moves[direction_key]
            old_x, old_y = player.pos_x, player.pos_y
            success = False
            # 1. Determine target coordinates
            if is_jumping:
                target_x, target_y = player.pos_x + (dx * 2), player.pos_y + (dy * 2)
            else:
                target_x, target_y = player.pos_x + dx, player.pos_y + dy

            # 2. Run the Exit Check
            if is_exit_blocked(g, target_x, target_y, inventory):
                score -=2 # Stay put, will trigger the "Bump" message below
                continue
            else:
                # 3. If not blocked by Exit, try to move/jump
                if is_jumping:
                    success = player.jump(dx, dy, g)
                elif player.can_move(dx, dy, g):
                    player.pos_x, player.pos_y = target_x, target_y
                    success = True

            if success:
                score -= 1
                if g.get(old_x, old_y) not in ["X", "E", "C", "K"]:
                    g.set(old_x, old_y, "~")
                new_x, new_y = player.pos_x, player.pos_y
                tile_content = g.get(new_x, new_y)
                item_found = False

                if isinstance(tile_content, pickups.SpecialItem) and tile_content.name == "Key":
                    inventory.append("Key")
                    print("🔑 You found a KEY!")
                    g.clear(new_x, new_y)
                    item_found = True  # This prevents losing a move point if you like

                    # 2. Opening a Chest
                elif tile_content == "C":
                    if "Key" in inventory:
                        inventory.remove("Key")
                        score += 100
                        print("🎁 TREASURE! Chest opened! +100 points")
                        g.clear(new_x, new_y)
                        item_found = True
                    else:
                        print("🔒 Locked! You need a key 'k'.")
                        continue  # Stops player from moving onto the chest without a key
                # --- KEY & CHEST LOGIC END ---
                elif tile_content == "E":
                    if len([i for i in inventory if i != "Key"]) >= 7:
                        print("\nVICTORY! You reached the exit with all fruits!")
                        break
                    else:
                        print(f"\nExit locked 🔒 until all fruits are collected!.")
                        # Don't move onto the exit tile if it's locked to avoid overwriting it with lava
                        continue

                elif isinstance(tile_content, pickups.Item):
                    score += tile_content.value
                    inventory.append(tile_content.name)
                    grace_steps = 5  # <--- NEW: Grant 5 protected steps
                    item_found = True
                    print(f"You found a {tile_content.name}, +{tile_content.value} points. ")
                    g.clear(new_x, new_y)

                        # Hazard & Scoring Logic
                if grace_steps > 0:
                    print("🛡️ Grace Period active!")
                    if not item_found: grace_steps -= 1
                else:
                    if tile_content == "X":
                        score -= 10; print("💥 Trap! 'X' -10 points")
                    elif tile_content == "~":
                        score -= 5; print("🔥 Lava! '~' -5 points")
                    elif not item_found:
                        score -= 1  # Movement cost

                        # Move and leave trail
                if g.get(player.pos_x, player.pos_y) not in ["X", "E"]:
                    g.set(player.pos_x, player.pos_y, "~")


                player.pos_x = new_x
                player.pos_y = new_y

                move_count += 1
                # 3. Post-move events (Bombs & Spawning)
                score -= handle_explosions(g, active_bombs, (player.pos_x, player.pos_y))

                if move_count % 25 == 0:
                    if pickups.spawn_single_fruit(g):
                        print("\n✨ The soil is fertile! A new fruit has sprouted somewhere! ✨")
                if score < 0:
                    print("\nGAME OVER: You stayed in the lava too long!")
                    break
            else:
                print("\nOOPS! You bumped into a wall -2 points!")
                score -=2

                #elif command in moves:
        else:
            # This triggers only if the command was a move but can_move returned False
            print("\nOOPS! Wrong move -2 points!")
            score -= 2  # Optional: penalty for bumping into walls

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

if __name__ == "__main__":
    play_game()