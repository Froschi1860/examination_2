import card, deck, cardHand, time, player


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.p1_hand = None
        self.p2_hand = None
        self.game_over = False
        self.game_winner = None
        self.game_loser = None
        self.rounds = 0


    def print_card(self, p1_card, p2_card, print_info, pot):
        self.check_winner(self.p1_hand, self.p2_hand)
        if not self.game_over:
            p1_card, p2_card = self.p1_hand.pop(0), self.p2_hand.pop(0)
    
            print(f"\n{f'{self.player_1}':<12}|{f' {self.player_2}':<12}\n------------|------------" if print_info else "")
            
            l1 = p1_card.ascii_card.split('\n')
            l2 = p2_card.ascii_card.split('\n')
    
            for i in range(min(len(l1), len(l2))):
                print(l1[i] + "   " + l2[i])
    
            pot.append(p1_card)
            pot.append(p2_card)
    
        return p1_card, p2_card


    def print_card_war(self, p1_card, p2_card, pot, sleep_time=0.5):
        for i in range(3):
            self.check_winner(self.p1_hand, self.p2_hand)
            if not self.game_over:
                p1_card, p2_card = self.p1_hand.pop(0), self.p2_hand.pop(0)
    
                l1 = p1_card.ascii_hidden.split('\n')
                l2 = p2_card.ascii_hidden.split('\n')
    
                for i in range(min(len(l1), len(l2))): print(l1[i] + "   " + l2[i])
    
                pot.append(p1_card)
                pot.append(p2_card)
                time.sleep(sleep_time)

        return p1_card, p2_card


    def check_winner(self, p1_hand, p2_hand):
        if len(p1_hand) == 0:
            self.game_winner = self.player_2
            self.game_loser = self.player_1
            self.game_over = True
        elif len(p2_hand) == 0:
            self.game_winner = self.player_1
            self.game_loser = self.player_2
            self.game_over = True

    
    def sort_cards(self, pot, winner):
        print(f"{winner}, you can sort the pot before continuing")
        while True:
            for i in pot: print(i.classic, end=f": {pot.index(i)} | ")
            print()
            print("Input SWITCH to switch cards | DONE when you are finish: ", end=" ")
            res = input()
            if res.upper() == "SWITCH":
                print("Input first card position (int): ", end="")
                card1_pos = int(input())
                print("Input second card position (int): ", end="")
                card2_pos = int(input())
                if (card1_pos >= 0 and card1_pos <= len(pot)) and (card2_pos >= 0 and card2_pos <= len(pot)):
                    pot[card1_pos], pot[card2_pos] = pot[card2_pos], pot[card1_pos]
            elif res.upper() == "DONE": return pot


    def end_game(self):
        self.game_winner.update_player_stats(True, self.rounds)
        self.game_loser.update_player_stats(False, self.rounds)
        player.write_player_data(player.player_list, 'src/Player_stats.json')

    
    def draw(self, simulate=False):
        while not self.game_over:
            pot = []
            p1_card, p2_card, winner = None, None, None
            p1_card, p2_card = self.print_card(p1_card, p2_card, True, pot)

            while (p1_card.value == p2_card.value) or (p1_card.suit == p2_card.suit) and not self.game_over:
                self.check_winner(self.p1_hand, self.p2_hand)
                if not self.game_over:
                    print("--- THERE IS A WAR ---")
                    if simulate: 
                        p1_card, p2_card = self.print_card_war(p1_card, p2_card, pot, 0)
                    else:
                        time.sleep(1)
                        p1_card, p2_card = self.print_card_war(p1_card, p2_card, pot)
                    p1_card, p2_card = self.print_card(p1_card, p2_card, False, pot)
    
            if p1_card.value > p2_card.value:
                winner = self.player_1
                if len(pot) > 2 and self.player_1.player_id != "com" and simulate == False: pot = self.sort_cards(pot, winner)
                [self.p1_hand.append(x) for x in pot]

            elif p1_card.value < p2_card.value:
                winner = self.player_2
                if len(pot) > 2 and self.player_2.player_id != "com" and simulate == False: pot = self.sort_cards(pot, winner)
                [self.p2_hand.append(x) for x in pot]

            print(f"{winner} wins the round !")
            self.rounds += 1
            self.check_winner(self.p1_hand, self.p2_hand)

            if not simulate: break
        if self.game_over: print(f"\n{self.game_winner} wins the game !")


    def start(self):
        self.p1_hand, self.p2_hand = deck.Deck.deal_cards(deck.Deck().deck)
        print(self.player_1, self.player_2)
        
        while not self.game_over:
            print("Press ENTER to draw, Type EXIT to quit game or CHEAT to simulate the game: ", end="")
            res = input()

            if res == "": self.draw()
            elif res.upper() == "EXIT": return
            elif res.upper() == "CHEAT": self.draw(True)
        self.end_game()
        return True
