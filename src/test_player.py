import unittest
import player
from unittest.mock import patch, mock_open
import json
class testPlayer(unittest.TestCase):
    
    
    # def setUp(self):
    #     '''creates a default player for testing each class'''
    #     pass
    
    # def tearDown(self):
    #     '''removes default player for testing each class'''
    #     pass
    
    #testing init
    def test_init_with_one_argument(self):
        '''test that a player object is made with just one argument'''
    
    
    def test_init_with_two_arguments(self):
        '''test player with two arguments '''
    
    
    def test_init_with_three_arguments(self):
        '''test player with three arguments '''
    
    
    def test_init_with_four_arguments(self):
        '''test player with four arguments '''


    def test_init_with_five_arguments(self):
        '''test player with five arguments '''

 
    def test_init_with_all_arguments(self):
        '''test player with all arguments '''    

    
    #testing changing player id
    def test_change_player_id(self):
        '''test that a player's id is changed'''

    
    #testing updating player stats 
    def test_update_statistics_game_won(self):
        '''test updates statistics for a winning game'''
    
    
    def test_update_statistics_game_lost(self):
        '''test updates statistics for a losing game'''
        
    #test to String method
    def test_return_player_id_as_string(self):
        '''tests that the selected player's name is returned as a string'''
    
    
    #test choose player
    def test_choose_existing_player(self):
        '''tests that a player from the player list is chosen'''
    
    
    def test_choose_non_existing_player(self):
        '''tests that nothing is returned if a player that does not exist is chosen'''
    
    
    #test player id 
    def test_check_player_id_exists(self):
        '''tests that it returns true if a player who is already on the list exists'''
    
    
    def test_check_player_id_not_exists(self):
        '''tests that it returns false if a player is not already on the list'''

    #test add player 
    
    def test_player_is_added_one_argument(self):
        '''tests if a new player is added to the player list with default stats'''

    
    def test_player_is_added_two_arguments(self):
        '''tests that a new player is still added with default stats even if multiple arguments are given'''

    
    #test write player data 
    
    def test_write_player_data(self):
        '''tests if data from the player list is saved into a JSON file'''
        with patch ('player.write_player_data') as mocked_file:
            pass
    
    #test read player data
    
    
    def test_read_player_data_with_existing_file(self):
        '''tests if data is read and from a json file and added into the player list'''
        
    
    def test_read_player_data_with_no_file(self):
        '''tests to see if when no data is found from a json file the player list remains empty'''
    

if __name__ == '__main__':
    unittest.main
