import random

# Blackjack Game - Team Project
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculates score, checking for Blackjack and Ace conversion."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Represents Blackjack

    # Convert Ace from 11 to 1 if score exceeds 21
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)
