import itertools, card, cardHand, random

class Deck:
    def __init__(self):
        figs, suits = ["J", "Q", "K", "A"], ["\u2665", "\u2660", "\u2666", "\u2663"]

        self.deck = [card.Card(figs[num-11] if num in range(11, 15) else num, suits[suit], num) for suit, num in itertools.product(range(4), range(2, 15))]
        random.shuffle(self.deck)


def deal_cards(deck): return cardHand.CardHand(deck, 0).cardHand, cardHand.CardHand(deck, 1).cardHand