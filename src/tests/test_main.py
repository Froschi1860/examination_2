import unittest
import sys
sys.path.append(".")
from src.game import card

class TestGameClass(unittest.TestCase):
    def test_card(self):
        carte = card.Card("K", "\u2665", 13)

if __name__ == "__main__": 
    unittest.main()