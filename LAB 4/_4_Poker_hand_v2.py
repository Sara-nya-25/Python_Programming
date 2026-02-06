"""
Build the first version of poker_hand(cards).Continue adding more checks to the function.
Tip! You can make a function that prints the card value more nicely:
pretty_print_card(["hearts", 5]) → "hearts five"
List of poker hands.
One pair (two cards of the same value)
Two pair
Three of a kind (three of a kind)
Straight (5 cards in a row, e.g. 7-8-9-10-11)
Flush / color (all cards have the same color)
House (pairs and threes of different values)
Four of a kind
Straight flush (5 cards in a row, of the same color)
Five of a kind
"""
from collections import Counter
import random
def get_hand_stats(hand):
    values = sorted([card[1] for card in hand])
    suits = [card[0] for card in hand]
    value_counts = Counter(values) # e.g., {10: 2, 5: 1, 3: 2}
    return values, suits, value_counts


def analyze_poker_hand(hand):
    values, suits, counts = get_hand_stats(hand)

    # Check for Flush and Straight
    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and (values[-1] - values[0] == 4)

    # Get the frequencies (e.g., [3, 2] for a Full House)
    frequencies = sorted(counts.values(), reverse=True)

    if frequencies == [5]:
        return "Five of a Kind"
    if is_straight and is_flush:
        return "Straight Flush"
    if frequencies == [4, 1]:
        return "Four of a Kind"
    if frequencies == [3, 2]:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if frequencies == [3, 1, 1]:
        return "Three of a Kind"
    if frequencies == [2, 2, 1]:
        return "Two Pair"
    if frequencies == [2, 1, 1, 1]:
        return "One Pair"

    return "High Card"

my_hand = [
    ["hearts", 10],
    ["spades", 10],
    ["diamonds", 10],
    ["clubs", 5],
    ["hearts", 5]
]

def get_random_card():
    # Define the possible suits
    suits = ["diamonds", "hearts", "spades", "clubs"]

    # Randomly select a suit and a value between 2 and 14
    suit = random.choice(suits)
    value = random.randint(2, 14)

    # Return as a list with two elements
    return [suit, value]

random_hand = []
for i in range(5):
    random_hand.append(get_random_card())

# 2. Show the user what they have
print(f"Your Hand: {random_hand}")

# 3. Analyze it
hand_type = analyze_poker_hand(random_hand)
print(f"Result: {hand_type}")