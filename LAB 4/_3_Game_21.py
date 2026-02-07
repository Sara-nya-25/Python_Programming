"""
Possible further development: build a game that asks the user whether to take a new card or stand. (randomize a number)
Make the computer simulate an opponent. The goal is to beat the computer.
"""
import random
import time

player_total = 0
computer_total = 0
player_standing = False
computer_standing = False
c_bust = False
p_bust = False
print("--- Welcome to the Turn-Based 21 Game ---")

def draw_card():
    return random.randint(1, 11)

def play_game():
    global player_total, computer_total, player_standing, computer_standing
    global c_bust, p_bust
    # Game continues as long as someone hasn't busted AND someone is still hitting
    while player_total <= 21 and computer_total <= 21:
        
        # 1. PLAYER'S TURN
        if not player_standing:
            action = input(f"\nYour total: {player_total}. [H]it or [S]tand? ").lower()
            if action == 'h':
                card = draw_card()
                player_total += card
                print(f"You pulled a {card}. New total: {player_total}")
                if player_total > 21:
                    print("💥 BUST! You went over 21.")
                    p_bust = True
                    break
            else:
                print(f"You chose to Stand at {player_total}.")
                player_standing = True
        else:
            print(f"\nYou are standing at {player_total}.")

        # 2. COMPUTER'S TURN
        if computer_total <= 21 and not computer_standing:
            print("\nComputer is thinking...")
            time.sleep(1)
            
            # Computer logic: hit if under 17, otherwise stand
            if computer_total < 21:
                card = draw_card()
                computer_total += card
                print(f"Computer draws a {card}. Computer total: {computer_total}")
                if computer_total > 17:
                    print("🤖 Computer BUSTS!")
                    c_bust = True
                    break
            else:
                print("Computer chooses to Stand.")
                computer_standing = True
        else:
            if not computer_total > 17:
                print("\nComputer is standing.")

        # 3. CHECK IF BOTH ARE STANDING
        if player_standing and computer_standing:
            break

    # --- FINAL REVEAL ---
    print("\n--- FINAL RESULTS ---")
    print(f"Player: {player_total}")
    print(f"Computer: {computer_total}")
    if p_bust:
        print("💻 Computer wins! (You busted)")
        exit()
    elif c_bust:
        print("🏆 You win! (Computer busted)")
        exit()
    elif player_total > computer_total:
        print("🏆 Congratulations! You beat the computer!")
    elif computer_total > player_total:
        print("💻 The computer wins this round.")
    else:
        print("🤝 It's a draw!")

play_game()