import unittest
from xml.etree.ElementTree import tostring
import player
from unittest.mock import patch, mock_open
import json

test_player_list = []

class testPlayer(unittest.TestCase):
        
    def test_init_with_one_argument(self):
        '''test that a player object is made with just one argument'''
        test_player = player.Player("test")
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test" )
        self.assertTrue(test_player.last_rounds_played == 0)
        self.assertTrue(test_player.total_rounds_played == 0)
        self.assertTrue(test_player.games_played == 0)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)
        
        
    def test_init_with_two_arguments(self):
        '''test player with two arguments '''
        test_player = player.Player("test", 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test" )
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 0)
        self.assertTrue(test_player.games_played == 0)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)
    
    def test_init_with_three_arguments(self):
        '''test player with three arguments '''
        test_player = player.Player("test", 2, 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test" )
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 0)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)
    
    def test_init_with_four_arguments(self):
        '''test player with four arguments '''
        test_player = player.Player("test", 2, 2, 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test" )
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 2)
        self.assertFalse(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)


    def test_init_with_five_arguments(self):
        '''test player with five arguments '''
        test_player = player.Player("test", 2, 2, 2, True)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test" )
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 2)
        self.assertTrue(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 0)
 
    def test_init_with_all_arguments(self):
        '''test player with all arguments '''    
        test_player = player.Player("test", 2, 2, 2, True, 2)
        self.assertIsInstance(test_player, player.Player)
        self.assertTrue(test_player.player_id == "test" )
        self.assertTrue(test_player.last_rounds_played == 2)
        self.assertTrue(test_player.total_rounds_played == 2)
        self.assertTrue(test_player.games_played == 2)
        self.assertTrue(test_player.last_game_won)
        self.assertTrue(test_player.total_games_won == 2)

    
    #testing changing player id
    def test_change_player_id(self):
        '''test that a player's id is changed'''
        test_player = player.Player("test")
        new_id = "changed_id"
        test_player.change_player_id(new_id)
        self.assertEqual(test_player.player_id, "changed_id")
        self.assertNotEqual(test_player.player_id, "test")
    
    
    #testing updating player stats 
    def test_update_statistics_game_won(self):
        '''test updates statistics for a winning game'''
        test_player = player.Player("test")
        former_stats_wins = test_player.total_games_won
        former_stats_rounds= test_player.total_rounds_played
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
        '''test updates statistics for a losing game'''
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
        
    
    #test to String method
    # def test_return_player_id_as_string(self):
    #     '''tests that the selected player's name is returned as a string'''
    #     test_player = player.Player("test")
    #     self.assertEqual(str(test_player), test_player)
    #     #fails 
    #     pass
    
    
    #test choose player
    def test_choose_existing_player(self):
        '''tests that a player from the player list is chosen'''
        test_list = [{'Player ID': "test player 1", 'Total Games Won': 0,
            'Total Games Played': 1 , 'Total Rounds Played': 0, 
            'Last Game Won': True, 'Last Rounds Played': 0 }]
        test_player = player.Player("test")
        
        chosen_player = player.choose_player("test")
        self.assertEqual(test_player, chosen_player)



    def test_choose_non_existing_player(self):
        '''tests that nothing is returned if a player that does not exist is chosen'''
        test_player = player.Player("test")

        pass
    
    
    #test player id 
    def test_check_player_id_exists(self):
        '''tests that it returns true if a player who is already on the list exists'''
        test_player = player.Player("test")

        pass
    
    
    def test_check_player_id_not_exists(self):
        '''tests that it returns false if a player is not already on the list'''
        test_player = player.Player("test")

        pass
    
    
    #test add player 
    
    def test_player_is_added_one_argument(self):
        '''tests if a new player is added to the player list with default stats'''
        test_player = player.Player("test")
        
        pass
    
    
    def test_player_is_added_two_arguments(self):
        '''tests that a new player is still added with default stats even if multiple arguments are given'''
        test_player = player.Player("test")
        

        pass
    
    
    #test write player data 
    def test_write_player_data(self):
        '''tests if data from the player list is saved into a JSON file'''
        test_player = player.Player("test")
        pass
    
    #test read player data
    
    
    def test_read_player_data_with_existing_file(self):
        '''tests if data is read and from a json file and added into the player list'''
        pass
    
    
    def test_read_player_data_with_no_file(self):
        '''tests to see if when no data is found from a json file the player list remains empty'''
        pass
    
    
if __name__ == '__main__':
    unittest.main()
