"""This module contains tests for player.py."""
import unittest
import player
import json
from os.path import exists as file_exists
import os


class testPlayer(unittest.TestCase):
    """Tests for player.py."""

    def test_init_with_one_argument(self):
        """Test that a player object is made with just one argument."""
        test_player = player.Player("test")
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test")
        self.assertTrue(test_player.last_rounds_played == 0)
        self.assertTrue(test_player.total_rounds_played == 0)
        self.assertTrue(test_player.games_played == 0)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)

    def test_init_with_two_arguments(self):
        """Test player with two arguments."""
        test_player = player.Player("test", 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test")
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 0)
        self.assertTrue(test_player.games_played == 0)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)

    def test_init_with_three_arguments(self):
        """Test player with three arguments."""
        test_player = player.Player("test", 2, 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test")
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 0)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)

    def test_init_with_four_arguments(self):
        """Test player with four arguments."""
        test_player = player.Player("test", 2, 2, 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test")
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 2)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)

    def test_init_with_five_arguments(self):
        """Test player with five arguments."""
        test_player = player.Player("test", 2, 2, 2, True)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test")
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 2)
        self.assertTrue(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)

    def test_init_with_all_arguments(self):
        """Test player with all arguments."""
        test_player = player.Player("test", 2, 2, 2, True, 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test")
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 2)
        self.assertTrue(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 2)

    # testing changing player id
    def test_change_player_id(self):
        """Test that a player's id is changed."""
        test_player = player.Player("test")
        new_id = "changed_id"
        test_player.change_player_id(new_id)
        self.assertEqual(test_player.player_id, "changed_id")
        self.assertNotEqual(test_player.player_id, "test")

    # testing updating player stats
    def test_update_statistics_game_won(self):
        """Test updates statistics for a winning game."""
        test_player = player.Player("test")
        former_stats_wins = test_player.total_games_won
        former_stats_rounds = test_player.total_rounds_played
        former_stats_games = test_player.games_played
        test_winner = True
        test_rounds = 10
        test_player.update_player_stats(test_winner, test_rounds)
        self.assertEqual(test_player.player_id, "test")
        self.assertGreater(test_player.total_games_won, former_stats_wins)
        self.assertEqual(test_player.total_rounds_played, (former_stats_rounds + test_rounds))
        self.assertGreater(test_player.games_played, former_stats_games)
        self.assertEqual(test_rounds, test_player.last_rounds_played)
    
    def test_update_statistics_game_lost(self):
        """Test updates statistics for a losing game."""
        test_player = player.Player("test")
        former_stats_wins = test_player.total_games_won
        former_stats_rounds= test_player.total_rounds_played
        former_stats_games = test_player.games_played
        test_winner = False
        test_rounds = 10
        test_player.update_player_stats(test_winner, test_rounds)
        self.assertEqual(test_player.player_id, "test")
        self.assertEqual(test_player.total_games_won, former_stats_wins)
        self.assertEqual(test_player.total_rounds_played, (former_stats_rounds + test_rounds))
        self.assertGreater(test_player.games_played, former_stats_games)
        self.assertEqual(test_rounds, test_player.last_rounds_played)

    # test to String method
    def test_to_string(self):
        """Tests that when a player is printed it returns with their player id."""
        test_player = player.Player("test")
        self.assertEqual("test", str(test_player))

    # test choose player
    def test_choose_existing_player(self):
        """Tests that a player from the player list is chosen."""
        test_player = player.Player("test")
        player.add_player("test")
        chosen_player = player.choose_player("test")
        self.assertEqual(test_player.player_id, chosen_player.player_id)
        self.assertEqual(test_player.games_played, chosen_player.games_played)
        self.assertEqual(test_player.total_rounds_played, chosen_player.total_rounds_played)

    def test_choose_non_existing_player(self):
        """Tests that nothing is returned if a player that does not exist is chosen."""
        test_player = player.Player("test")
        chosen_player = player.choose_player("choose")
        self.assertIsNone(chosen_player)

    # test player id
    def test_check_player_id_exists(self):
        """Tests that it returns true if a player who is already on the list exists."""
        test_player = player.Player("test")
        player.add_player("test")
        id_check = player.check_player_id("test")
        self.assertTrue(id_check)

    def test_check_player_id_not_exists(self):
        """Tests that it returns false if a player is not already on the list."""
        id_check = player.check_player_id("random")
        self.assertFalse(id_check)

    # test add player
    def test_player_is_added_one_argument(self):
        """Tests if a new player is added to the player list."""
        test_player = player.Player("test")
        player.player_list = []
        player.add_player("test")
        player_as_dict = player.player_list[0]
        self.assertEqual(test_player.player_id, player_as_dict["Player ID"])

    # test write player data
    def test_write_player_data(self):
        """Tests if data from the player list is saved into a JSON file."""
        list_content = [
            {'Player ID': "test player 1", 'Total Games Won': 0,
            'Total Games Played': 1, 'Total Rounds Played': 0, 
            'Last Game Won': True, 'Last Rounds Played': 0}]
        player.write_player_data(list_content)
        self.assertTrue('Player_stats.json')
        os.remove('Player_stats.json')

    # test read player data
    def test_read_player_data_with_existing_file(self):
        """Tests if data is read and from a json file and added into the player list."""
        content = [{'Player ID': "test player 1", 'Total Games Won': 0,
            'Total Games Played': 1, 'Total Rounds Played': 0, 
            'Last Game Won': True, 'Last Rounds Played': 0}]
        with open('Player_stats.json', 'w') as test_file:
            json.dump(content,test_file)

        test_list = player.read_player_data()
        self.assertEqual(content, test_list)
        os.remove('Player_stats.json')

    def test_read_player_data_with_no_file(self):
        """Tests to see if when no data is found from a json file the player list remains empty."""
        no_values_list = []
        if file_exists('Player_stats.json'):
            os.remove('Player_stats.json')
        no_file_exists = player.read_player_data()
        self.assertEqual(no_values_list, no_file_exists)

if __name__ == '__main__':
    unittest.main()

