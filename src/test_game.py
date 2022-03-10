import unittest, card, deck, cardHand, time, player, game
from unittest.mock import patch


class test_game(unittest.TestCase):

    def setUp(self):
        self.test_game = game.Game(player.Player("vee"), player.Player("fabi"))
        self.test_game.p1_hand, self.test_game.p2_hand = deck.Deck.deal_cards(deck.Deck().deck)

    def test_init_default_values(self):
        """Test the init function with default variables"""
        the_game = game.Game("", "")
        self.assertIsInstance(the_game, game.Game)
        self.assertIsNone(the_game.p1_hand)
        self.assertIsNone(the_game.p2_hand)
        self.assertFalse(the_game.game_over)
        self.assertIsNone(the_game.game_winner)
        self.assertIsNone(the_game.game_loser)
        self.assertTrue(the_game.rounds == 0)


    def test_init_args(self):
        """Test the init function with arguments"""
        the_game = game.Game(player.Player("vee"), player.Player("fabi"))
        self.assertTrue(the_game.player_1.player_id == "vee")
        self.assertTrue(the_game.player_2.player_id == "fabi")


    @patch('builtins.input', return_value='cheat')
    def test_start(self, mock_input):
        """Test the start function with input of cheat"""
        the_game = game.Game(player.Player("User"), player.Player("com"))
        the_game.start()
        calling_1 = mock_input()
        self.assertTrue(calling_1 == 'cheat')   


    def test_card_war(self):
        """Test the print_card_war function"""
        card_1 = self.test_game.p1_hand.pop(0)
        card_2 = self.test_game.p1_hand.pop(0)
        pot = []

        exp_card_1 = self.test_game.p1_hand[0]
        exp_card_2 = self.test_game.p2_hand[0]
        exp_card_3 = self.test_game.p1_hand[1]
        exp_card_4 = self.test_game.p2_hand[1]
        exp_card_5 = self.test_game.p1_hand[2]
        exp_card_6 = self.test_game.p2_hand[2]

        card_1, card_2 = self.test_game.print_card_war(card_1, card_2, pot)
        self.assertIn(exp_card_1, pot)
        self.assertIn(exp_card_2, pot)
        self.assertIn(exp_card_3, pot)
        self.assertIn(exp_card_4, pot)
        self.assertIn(exp_card_5, pot)
        self.assertIn(exp_card_6, pot)
        
        self.assertEqual(card_1, exp_card_5)
        self.assertEqual(card_2, exp_card_6)


    def test_check_win_for_player_1(self): 
        """Test the check_winner function in case of player 1 win"""
        p1_hand_cleared = []
        self.test_game.check_winner(p1_hand_cleared, self.test_game.p2_hand)
        self.assertTrue(self.test_game.game_over)


    def test_check_win_for_player_2(self): 
        """Test the check_winner function in case of player 2 win"""
        p2_hand_cleared = []
        self.test_game.check_winner(self.test_game.p1_hand, p2_hand_cleared)
        self.assertTrue(self.test_game.game_over)


    def test_end_game(self):
        """Test the end_game function"""
        self.test_game.game_winner = self.test_game.player_1
        self.test_game.game_loser = self.test_game.player_2
        self.test_game.end_game()
        self.assertTrue(True)


    def test_draw(self):
        """Test the draw function"""
        self.test_game.draw(True)


    @patch('builtins.input', return_value='done')
    def test_sort_card(self, mock_input):
        """Test the sort_card function"""
        round_winner = self.test_game.player_1
        pot = [self.test_game.p1_hand[0], self.test_game.p1_hand[1], self.test_game.p2_hand[0], self.test_game.p2_hand[1]]
        self.test_game.sort_cards(pot, round_winner)
        calling_1 = mock_input()
        self.assertTrue(calling_1 == 'done')   



if __name__ == "__main__":
    unittest.main()