import cardHand, deck 

if __name__ == "__main__":

    # my_deck = deck.Deck().deck
    # for i in my_deck: print(i)

    p1_hand, p2_hand = deck.deal_cards(deck.Deck().deck)
    for i in p1_hand: print(i)
    print("--------")
    for i in p2_hand: print(i)

    deck_list = p1_hand + p2_hand
    print(len(deck_list))
    print(len(set(deck_list)))

    # menu_flag = True

    # while menu_flag:
    #     print("Press ENTER to draw", end="")
    #     res = input()

    #     if res == "":
    #         p1_card, p2_card = p1_hand.pop(), p2_hand.pop()
    #         print(f"""\nPlayer 1 | Player 2\n---------|---------\n{p1_card}      | {p2_card}\n""")

    #         print(f"{'Player 1' if p1_card.value > p2_card.value else 'Player 2'} wins the round!")