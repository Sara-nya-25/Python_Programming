import random
from collections import Counter

def get_random_card():
    suits = ["diamonds", "hearts", "spades", "clubs"]
    return [random.choice(suits), random.randint(2, 14)]

def get_hand_stats(hand):
    values = sorted([card[1] for card in hand])
    suits = [card[0] for card in hand]
    value_counts = Counter(values)
    return values, suits, value_counts

def analyze_poker_hand(hand):
    values, suits, counts = get_hand_stats(hand)
    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and (values[-1] - values[0] == 4)
    frequencies = sorted(counts.values(), reverse=True)

    if frequencies == [5]: return "Five of a Kind"
    if is_straight and is_flush: return "Straight Flush"
    if frequencies == [4, 1]: return "Four of a Kind"
    if frequencies == [3, 2]: return "Full House"
    if is_flush: return "Flush"
    if is_straight: return "Straight"
    if frequencies == [3, 1, 1]: return "Three of a Kind"
    if frequencies == [2, 2, 1]: return "Two Pair"
    if frequencies == [2, 1, 1, 1]: return "One Pair"
    return "High Card"

def play_poker_match():
    # Define hand rankings (Higher number = Stronger hand)
    rankings = {
        "High Card": 1, "One Pair": 2, "Two Pair": 3, "Three of a Kind": 4,
        "Straight": 5, "Flush": 6, "Full House": 7, "Four of a Kind": 8,
        "Straight Flush": 9, "Five of a Kind": 10
    }

    # Generate hands
    player1_hand = [get_random_card() for _ in range(5)]
    player2_hand = [get_random_card() for _ in range(5)]

    # Analyze hands
    p1_result = analyze_poker_hand(player1_hand)
    p2_result = analyze_poker_hand(player2_hand)

    # Print results
    print(f"Player 1 Hand: {player1_hand} -> {p1_result}")
    print(f"Player 2 Hand: {player2_hand} -> {p2_result}")
    print("-" * 30)

    # Compare using the rankings
    if rankings[p1_result] > rankings[p2_result]:
        print("🎉 Player 1 Wins!")
    elif rankings[p2_result] > rankings[p1_result]:
        print("🤖 Player 2 Wins!")
    else:
        print("🤝 It's a Tie (based on hand type)!")

play_poker_match()