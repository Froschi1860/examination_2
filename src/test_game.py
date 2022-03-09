import unittest, card, deck, cardHand, time, player, game
from unittest.mock import patch

class test_game(unittest.TestCase):

    def setUp(self):
        self.test_game = game.Game(player.Player("vee"), player.Player("fabi"))
        self.test_game.p1_hand, test_game.p2_hand = deck.Deck.deal_cards(deck.Deck().deck)

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
        card_1 = self.test_game.p1_hand.pop(0)
        card_2 = self.test_game.p1_hand.pop(0)
        self.test_game.print_card_war(card_1, card_2, pot=[])

if __name__ == "__main__":
    unittest.main()