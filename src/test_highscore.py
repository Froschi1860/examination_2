"""This modeule contains tests for highscore.py"""

import unittest
from unittest import mock
import highscore
import io
import sys
from unittest.mock import patch


class testHighscore(unittest.TestCase):
    """Tests for highscore.py"""
    
    def setUp(self):
        """sets up a mock list for the tests to run within the class"""
        self.test_player_list = [
            {'Player ID': "test player 1", 'Total Games Won': 0,
            'Total Games Played': 1 , 'Total Rounds Played': 0, 
            'Last Game Won': True, 'Last Rounds Played': 0 }, 
            
            {'Player ID':"test player 2" ,'Total Games Won': 1,
            'Total Games Played': 0 , 'Total Rounds Played': 0, 
            'Last Game Won': False, 'Last Rounds Played': 0 },
        
            {'Player ID':"test player 3" ,'Total Games Won': 4,
            'Total Games Played': 5, 'Total Rounds Played': 0, 
            'Last Game Won': False, 'Last Rounds Played': 0 }
            ]

        self.test_display_header = '''
HIGHSCORE RESULTS:\n
---------------------------------------------------------------------\n
PLAYER        | TOTAL WINS | TOTAL GAMES PLAYED | TOTAL ROUNDS PLAYED 
---------------------------------------------------------------------'''


# test initializer
    def test_init_function(self):
        """tests that the highscore object is made"""
        test_highscore = highscore.Highscore(self.test_player_list)
        self.assertIsInstance(test_highscore, highscore.Highscore)


    def test_init_with_empty_list(self):
        """tests the higscore object is made with an empty list"""
        test_highscore = highscore.Highscore([])
        self.assertIsInstance(test_highscore, highscore.Highscore)


 # test sort functionality
    def test_sort_score_results_by_winner(self):
        """tests that the first index is the one with the most games won and continues in decreasing order"""
        test_highscore = highscore.Highscore(self.test_player_list)
        test_scoreboard = test_highscore.sort_score_results()

        first_player_in_scoreboard = test_scoreboard[0]
        first_score = first_player_in_scoreboard[1]

        second_player_in_scoreboard = test_scoreboard[1]
        second_score = second_player_in_scoreboard[1]

        third_player_in_scoreboard = test_scoreboard[2]
        third_score = third_player_in_scoreboard[1]

        self.assertGreater(first_score, second_score)
        self.assertGreater(second_score, third_score)


    def test_length_scoreboard_stats(self):
        """tests that each player within the scoreboard only contains 4 statistics"""
        test_highscore = highscore.Highscore(self.test_player_list)
        test_scoreboard = test_highscore.sort_score_results()
        self.assertEqual(len(test_scoreboard[0]), 4)
        self.assertEqual(len(test_scoreboard[1]), 4)
        self.assertEqual(len(test_scoreboard[2]), 4)
        self.assertGreater(len(test_scoreboard[0]),3)
        self.assertLess(len(test_scoreboard[0]),5)


    def test_player_in_scoreboard(self):
        """tests that a player appears within the highscore"""
        test_highscore = highscore.Highscore(self.test_player_list)
        test_scoreboard = test_highscore.sort_score_results()
        scoreboard_player = test_scoreboard[0]
        winning_player = self.test_player_list[2]
        player_name = winning_player['Player ID']
        self.assertIn(player_name, scoreboard_player)


# test display scoreboard
    def test_display_scoreboard_results(self):
        """tests that the desired display will be output to the user"""
        test_highscore = highscore.Highscore(self.test_player_list)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_highscore.display_highscore()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        desired_output = self.test_display_header + """
test player 3  4            5                     0                    
test player 2  1            0                     0                    
test player 1  0            1                     0                    \n"""
        self.assertTrue(printed_output != "")
        self.assertEqual(printed_output, desired_output)


    def test_empty_scoreboard(self):
        """tests that an empty output is printed if no users are created"""
        empty_list = []
        test_highscore = highscore.Highscore(empty_list)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_highscore.display_highscore()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        empty_display = self.test_display_header + '\n'
        self.assertEqual(printed_output, empty_display)


if __name__ == '__main__':
    unittest.main()
