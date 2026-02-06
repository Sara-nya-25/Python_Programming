"""
1 Build a function that randomizes a playing card.
It should return a list with two elements: suit and value.
Suit can be: diamonds, hearts, spades or clubs. Value can be two to ace, for simplicity we use the numbers 2 to 14.
Example of a card: ["hearts", 12]
"""
import random
def get_random_card():
    # Define the possible suits
    suits = ["diamonds", "hearts", "spades", "clubs"]

    # Randomly select a suit and a value between 2 and 14
    suit = random.choice(suits)
    value = random.randint(2, 14)

    # Return as a list with two elements
    return [suit, value]


# Testing the function
new_card = get_random_card()
print(new_card)

print("\nCompare two cards and tell if they have same value")
def compare_cards(card1, card2):
    if card1[1] == card2[1]:
        return True
    else:
        return False

# Example usage:
card_a = ["hearts", 12]
card_b = ["spades", 12]
card_c = ["diamonds", 5]
print(f"Card A:{card_a}, Card B:{card_b}, Card C:{card_c}")
print(f"Are A and B the same? {compare_cards(card_a, card_b)}")
print(f"Are A and C the same? {compare_cards(card_a, card_c)}")

print("Check if there are 2 cards of same value")


def poker_hand(hand):
    # We will keep a list of values we have already looked at
    seen_values = []

    for card in hand:
        # card[1] is the numerical value (2-14)
        value = card[1]

        if value in seen_values:
            # We found a value that was already in our 'seen' list!
            return True

        # If not seen yet, add it to the list and keep looking
        seen_values.append(value)

    # If the loop finishes without finding a duplicate
    return False


# --- Setup for testing ---
# Hand with a pair of 12s (Queens)
hand_1 = [["hearts", 12], ["spades", 2], ["diamonds", 12], ["clubs", 5], ["hearts", 9]]

# Hand with no pairs
hand_2 = [["hearts", 10], ["spades", 2], ["diamonds", 14], ["clubs", 5], ["hearts", 9]]

print(f"Hand 1 has a pair: {poker_hand(hand_1)}")  # True
print(f"Hand 2 has a pair: {poker_hand(hand_2)}")  # False