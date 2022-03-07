'''This class constructs a player and adds them to a list of dictionaries which contains information about each player object.
This allows the user to select a player, make a new player, or even change the name of their already saved player'''

import json
from os.path import exists as file_exists
player_list = []


class Player:
    
    
    def __init__(self, player_id, last_rounds_played=0, total_rounds_played=0, games_played=0, 
                 last_game_won=False, total_games_won=0):
        '''construct player object, defaults set so that player info can be overrided as they increase their stats'''
        self.player_id = player_id
        self.last_rounds_played = last_rounds_played
        self.total_rounds_played = total_rounds_played
        self.games_played = games_played
        self.last_game_won = last_game_won
        self.total_games_won = total_games_won

    
    def change_player_id(self,new_player_id):
        '''allows the player to change their id'''
        for player in player_list:
            if player['Player ID'] == self.player_id:
                player['Player ID'] = new_player_id
        self.player_id = new_player_id
        
        
    def update_player_stats(self, player_id): 
        '''update player object as well as the player dictionary in the list'''
        if self.last_game_won == True:
            add_game = 1
        else:
            add_game = 0
               
        for player in player_list:
            if player['Player ID'] == player_id:
                self.last_game_won = False
                self.games_played =+ 1
                self.total_rounds_played += self.last_rounds_played
                player['Total Games Played'] = self.games_played 
                player['Total Rounds Played'] += self.total_rounds_played
                player['Total Games Won'] += add_game
                player['Last Game Won'] = self.last_game_won
                self.last_rounds_played = 0 
                player['Last Rounds Played'] = self.last_rounds_played

    
    def __str__(self):
        '''returns a string with the name of the player when called'''
        return f"{self.player_id}"


def choose_player(player_id):
    '''allows a player to be chosen from a list of already existed player, and for their updated statistics
    to be used within the game'''
    for player in player_list:
        if player['Player ID'] == player_id:
                selected_player = Player(player_id=player_id, last_rounds_played = player['Last Rounds Played'], 
                total_rounds_played=player['Total Rounds Played'], games_played=player['Total Games Played'],
                last_game_won=False, total_games_won= player['Total Games Won'])
                return selected_player


def check_player_id(player_id):
    '''checks to see if the player already has stats'''
    return_value = False
    for player in player_list:
        if player['Player ID'] == player_id:
            return_value = True
    return return_value 

def add_player(player_id):
    '''adds a new player to the player stats list'''
    player_stats = {'Player ID': player_id, 'Total Games Won': 0,
                    'Total Games Played': 0 , 'Total Rounds Played': 0, 
                    'Last Game Won': False, 'Last Rounds Played': 0 }
    player_list.append(player_stats)
    


def write_player_data(player_list):
     '''This method creates a file which is then used to store the player list outside of each game'''
     if file_exists('Player_stats.json'):
        pass
     else: 
         json.dump(player_list)
         
     try:
        with open('Player_stats.json', 'w') as file:
            json.dump(player_list, file)
        
     except FileNotFoundError:
         return 'There does not seem to be a saved file' 
             

def read_player_data():
    try:
        if file_exists('Player_stats.json'): 
            with open('Player_stats.json', 'r') as file:
                player_list = json.load(file)
                return player_list
        else:
            return player_list
    except FileExistsError:
        return player_list


