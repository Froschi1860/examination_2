"""This module constructs a player and adds them to a list of dictionaries
which contains information about each player object.Within the module one can
choose and check a player object, which is then read and written into a local
json file as well as aplayer list.
"""

import json
from os.path import exists as file_exists


player_list = []


class Player:
    """Within this class a player object is made, as well as the statistics of said player can be altered."""

    def __init__(self, player_id, last_rounds_played=0, total_rounds_played=0, games_played=0,
                last_game_won=False, total_games_won=0):
        """Construct player object, defaults set so that player info can be overrided as they increase their stats."""
        self.player_id = player_id
        self.last_rounds_played = last_rounds_played
        self.total_rounds_played = total_rounds_played
        self.games_played = games_played
        self.last_game_won = last_game_won
        self.total_games_won = total_games_won

    def change_player_id(self,new_player_id):
        """Allows the player to change their id."""
        for player in player_list:
            if player['Player ID'] == self.player_id:
                player['Player ID'] = new_player_id
        self.player_id = new_player_id

    def update_player_stats(self, is_winner, rounds_played):
        """Update player object as well as the player dictionary in the list."""
        if is_winner == True:
            self.total_games_won += 1
            self.last_game_won = True
        else:
            self.last_game_won = False

        self.last_rounds_played = rounds_played
        self.games_played += 1
        self.total_rounds_played += self.last_rounds_played
        for player in player_list:
            if player['Player ID'] == self.player_id:
                player['Total Games Played'] = self.games_played
                player['Total Rounds Played'] = self.total_rounds_played
                player['Total Games Won'] = self.total_games_won
                player['Last Game Won'] = self.last_game_won
                player['Last Rounds Played'] = self.last_rounds_played

    def __str__(self):
        """Returns a string with the name of the player when called."""
        return f"{self.player_id}"


def choose_player(player_id):
    """Allows a player to be chosen from a list of already existed player, and for their updated statistics
    to be used within the game."""
    for player in player_list:
        if player['Player ID'] == player_id:
            selected_player = Player(player_id=player_id, last_rounds_played=player['Last Rounds Played'],
            total_rounds_played=player['Total Rounds Played'], games_played=player['Total Games Played'],
            last_game_won=False, total_games_won= player['Total Games Won'])
            return selected_player


def check_player_id(player_id):
    """Checks to see if the player already has stats."""
    return_value = False
    for player in player_list:
        if player['Player ID'] == player_id:
            return_value = True
    return return_value


def add_player(player_id):
    """Adds a new player to the player stats list."""
    player_stats = {'Player ID': player_id, 'Total Games Won': 0,
                    'Total Games Played': 0 , 'Total Rounds Played': 0,
                    'Last Game Won': False, 'Last Rounds Played': 0 }
    player_list.append(player_stats)


def write_player_data(player_list):
    """This method creates a file which is then used to store
    the player list outside of each game."""
    try:
        with open('Player_stats.json', 'w') as file:
            json.dump(player_list, file)

    except FileNotFoundError:
        return 'There does not seem to be a saved file'


def read_player_data():
    """This method reads data from an already existing json file if the user
    has played the game before."""
    empty_player_list = []
    try:
        if file_exists('Player_stats.json'):
            with open('Player_stats.json', 'r') as file:
                player_list = json.load(file)
                return player_list
        else:
            return empty_player_list

    except FileExistsError:
        return player_list
