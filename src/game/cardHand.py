import deck

class CardHand: 
    def __init__(self, deck, i): 
        self.cardHand = [x for x in deck if list(deck).index(x) % 2 == i]