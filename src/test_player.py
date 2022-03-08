import unittest
import player
from unittest.mock import patch, mock_open
import json
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
        pass
    
    #testing updating player stats 
    def test_update_statistics_game_won(self):
        '''test updates statistics for a winning game'''
        pass
    
    def test_update_statistics_game_lost(self):
        '''test updates statistics for a losing game'''
        pass
        
    #test to String method
    def test_return_player_id_as_string(self):
        '''tests that the selected player's name is returned as a string'''
        pass
    
    #test choose player
    def test_choose_existing_player(self):
        '''tests that a player from the player list is chosen'''
        pass

    def test_choose_non_existing_player(self):
        '''tests that nothing is returned if a player that does not exist is chosen'''
        pass
    
    #test player id 
    def test_check_player_id_exists(self):
        '''tests that it returns true if a player who is already on the list exists'''
        pass
    
    def test_check_player_id_not_exists(self):
        '''tests that it returns false if a player is not already on the list'''
        pass
    
    
    #test add player 
    
    def test_player_is_added_one_argument(self):
        '''tests if a new player is added to the player list with default stats'''
        pass
    
    
    def test_player_is_added_two_arguments(self):
        '''tests that a new player is still added with default stats even if multiple arguments are given'''
        pass
    
    
    #test write player data 
    def test_write_player_data(self):
        '''tests if data from the player list is saved into a JSON file'''
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
