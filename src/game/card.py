class Card:
    def __init__(self, number, suit, value):
        self.number = number
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} {self.number}"