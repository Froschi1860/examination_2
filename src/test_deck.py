import itertools
import random
import unittest, card, deck, cardHand, time, player, game

class test_deck(unittest.TestCase):
    def test_init_deck(self):
        """Test the init function"""
        the_deck = deck.Deck()
        self.assertIsInstance(the_deck, deck.Deck)
        self.assertTrue(the_deck.figs == ["J", "Q", "K", "A"] and the_deck.suits == ["\u2665", "\u2660", "\u2666", "\u2663"])
        random.shuffle(the_deck.deck) 

    def test_deal_cards(self):
        """Test the deal cards function"""
        the_deck = deck.Deck()


if __name__ == "__main__":
    unittest.main()