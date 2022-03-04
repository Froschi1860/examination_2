import card, deck, cardHand, time


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.p1_hand = None
        self.p2_hand = None

    def print_card(self, p1_card, p2_card, print_info, pot):
        self.check_winner(self.p1_hand, self.p2_hand)
        p1_card, p2_card = self.p1_hand.pop(0), self.p2_hand.pop(0)
        print(f"\n{'Player 1':<12}|{' Player 2':<12}\n------------|------------" if print_info else "")
        l1 = p1_card.ascii_card.split('\n')
        l2 = p2_card.ascii_card.split('\n')
        for i in range(min(len(l1), len(l2))):
            print(l1[i] + "   " + l2[i])
        pot.append(p1_card)
        pot.append(p2_card)
        return p1_card, p2_card


    def print_card_war(self, p1_card, p2_card, pot):
        for i in range(3):
            self.check_winner(self.p1_hand, self.p2_hand)
            p1_card, p2_card = self.p1_hand.pop(0), self.p2_hand.pop(0)
            l1 = p1_card.ascii_hidden.split('\n')
            l2 = p2_card.ascii_hidden.split('\n')
            for i in range(min(len(l1), len(l2))):
                print(l1[i] + "   " + l2[i])
            pot.append(p1_card)
            pot.append(p2_card)
            time.sleep(0.5)
        return p1_card, p2_card


    def check_winner(self, p1_hand, p2_hand):
        if len(p1_hand) == 0:
            print("\nPlayer 1 wins the game !")
            exit()
        elif len(p2_hand) == 0:
            print("\nPlayer 2 wins the game !")
            exit()


    def start(self):
        self.p1_hand, self.p2_hand = deck.Deck.deal_cards(deck.Deck().deck)
        while True:
            print("Press ENTER to draw", end="")
            res = input()
            if res == "":
                pot = []
                p1_card, p2_card, winner = None, None, None
                p1_card, p2_card = self.print_card(p1_card, p2_card, True, pot)
                while (p1_card.value == p2_card.value) or (p1_card.suit == p2_card.suit):
                    print("--- THERE IS A WAR ---")
                    time.sleep(1)
                    p1_card, p2_card = self.print_card_war(p1_card, p2_card, pot)
                    p1_card, p2_card = self.print_card(p1_card, p2_card, False, pot)
                if p1_card.value > p2_card.value:
                    winner = "Player 1"
                    [self.p1_hand.append(x) for x in pot]
                elif p1_card.value < p2_card.value:
                    winner = "Player 2"
                    [self.p2_hand.append(x) for x in pot]
                print(f"{winner} wins the round !")
                self.check_winner(self.p1_hand, self.p2_hand)