import cardHand, deck 

def deal_cards(deck):
    player1_hand = cardHand.CardHand(deck, 0).cardHand
    player2_hand = cardHand.CardHand(deck, 1).cardHand
    for i in player1_hand: print(i.suit, i.number)
    print("\n-----------\n")
    for i in player2_hand: print(i.suit, i.number)

if __name__ == "__main__":
    deal_cards(deck.Deck().deck)
    print(__package__)