import itertools, card

class Deck:
    def __init__(self):
        self.deck = set()
        figures = ["J", "Q", "K", "A"]
        suits = ["\u2665", "\u2660", "\u2666", "\u2663"]

        for suit, number in itertools.product(range(4), range(2, 15)):
            self.deck.add(card.Card(figures[number-11] if number in range(11, 15) else number, suits[suit], number))