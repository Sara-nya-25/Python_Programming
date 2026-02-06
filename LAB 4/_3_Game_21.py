"""
Possible further development: build a game that asks the user whether to take a new card or stand. (randomize a number)
Make the computer simulate an opponent. The goal is to beat the computer.
"""
import random
import time
def draw_card():
    return random.randint(1, 13)


def play_game():
    print("--- Welcome to the 21 Game ---")
    player_total = 0
    computer_total = 0

    # Player's Turn
    while player_total <= 21:
        action = input(f"\nYour total is {player_total}. [H]it or [S]tand? ").lower()

        if action == 'h':
            card = draw_card()
            player_total += card
            print(f"You pulled a {card}. New total: {player_total}")
            if player_total > 21:
                print("💥 BUST! You went over 21.")

        elif action == 's':
            print(f"You stand at {player_total}.")
            break
        else:
            print("Invalid input, please type 'h' or 's'.")

        # --- COMPUTER'S TURN ---
        # Only happens if player didn't bust
    print("\n" + "=" * 20)
    print("Computer's turn...")
    time.sleep(1)  # Adds suspense

    while computer_total < 17:
        card = draw_card()
        computer_total += card
        print(f"Computer draws a {card}...")
        time.sleep(1)
        print(f"Computer total: {computer_total}")

        if computer_total > 21:
            print("🤖 Computer BUSTS! You win!")


    # --- FINAL REVEAL ---
    print("\n--- FINAL RESULTS ---")
    print(f"Player: {player_total}")
    print(f"Computer: {computer_total}")

    if player_total > computer_total:
        print("🏆 Congratulations! You beat the computer!")
    elif computer_total > player_total:
        print("💻 The computer wins this round.")
    else:
        print("🤝 It's a draw!")


# Run the game
play_game()


