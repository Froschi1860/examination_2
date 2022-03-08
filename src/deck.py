import itertools, card, cardHand, random

class Deck:
    def __init__(self):
        """Initializor that create the deck"""
        self.figs, self.suits = ["J", "Q", "K", "A"], ["\u2665", "\u2660", "\u2666", "\u2663"] # Store the figures and suits

        # Create the deck with 2 nested loops (create the 13 cards for each suits)
        self.deck = [card.Card(self.figs[num-11] if num in range(11, 15) else num, self.suits[suit], num) for suit, num in itertools.product(range(4), range(2, 15))]
        random.shuffle(self.deck)



    def deal_cards(deck): 
        """Deal the cards, divide the deck between the two players"""
        return cardHand.CardHand(deck, 0).cardHand, cardHand.CardHand(deck, 1).cardHand