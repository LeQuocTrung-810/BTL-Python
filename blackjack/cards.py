import random

class Card:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♠', '♣', '♥', '♦']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

class BJ_Card(Card):
    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 1
        else:
            return int(self.rank)

class BJ_Deck:
    def __init__(self):
        self.cards = [BJ_Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None
