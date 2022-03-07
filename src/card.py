class Card:
    def __init__(self, number, suit, value):
        self.number = number
        self.suit = suit
        self.value = value
        self.ascii_card = f"""┌─────────┐\n| {self.suit}       |\n|         |\n|         |\n|    {self.number:<2}   |\n|         |\n|         |\n|       {self.suit} |\n└─────────┘"""
        self.ascii_hidden = f"""┌─────────┐\n|#########|\n|#########|\n|#########|\n|#########|\n|#########|\n|#########|\n|#########|\n└─────────┘"""
        self.classic = f"{suit}{number}"

    def __str__(self):
        return self.ascii_card