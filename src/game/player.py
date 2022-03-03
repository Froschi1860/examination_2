import csv
from csv import DictWriter

# def createfile():
#     '''Create Player_Stats CSV file that we can work with'''
#     filename = 'Player_stats.csv'
#     header = ['Player ID', 'Total Wins', 'Total Games Played', 'Total Rounds Played' ]
#     with open (filename, 'w') as file: 
#         writer = csv.writer(file)
#         writer.writerow(header)


class Player:
    
    def __init__(self, player_id, last_rounds_played=0, total_rounds_played=0, games_played=0, last_game_won=False, total_games_won=0):
        '''construct player object, defaults set so that player info can be overrided as they increase their stats'''
        self.player_id = player_id
        self.last_rounds_played = last_rounds_played
        self.total_rounds_played = total_rounds_played
        self.games_played = games_played
        self.last_game_won = last_game_won
        self.total_games_won = total_games_won


    def check_player_id(self, player_id, path ='Player_stats.csv'):
        '''checks to see if the player already has stats'''
        with open(path, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            # Not sure if it works like this because it seems to return True/False once for each row
            # Maybe use a variable to return in the loop, set it True if the player_id exists and return it after the loop?
            for row in reader:
                if player_id == row[0]:
                    return True 
                else:
                    return False 

    def add_player(self, player_id, path = 'Player_stats.csv',):
        '''adds a player to the player stats file'''
        player_stats = [player_id,self.total_games_won, self.games_played, self.total_rounds_played]
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(player_stats)
            file.close()

    def update_player_stats(player_id,last_game_won, last_rounds_played, path = 'Plater_stats.csv'):
        # Not sure if I´m correct about this but is it even necessary to read the file in this function?
        # The function is called in the end of a game where two player objects already exist in the program
        # and both need to be updated -> Both should then already have the current instance variables at the
        # state before the game -> Then the function would need to update the variables that are already ints
        # and override the data in the file
        with open(path, 'r') as scoreboard:
            dict_reader = csv.DictReader(scoreboard)
            for row in dict_reader:
                if player_id == row['Player ID']:
                    wins = int(row['Total Wins']) 
                    games = int(row['Total Games Played'])
                    rounds = int(row['Total Rounds Played'])
                    
        if last_game_won == True:
            wins = wins + 1  
            
        games = games + 1
        rounds = rounds + last_rounds_played
        # Maybe to override the file it is necessary to create a new temoprary file holding the updated 
        # data, then to delete the original file and lastly to rename the temorary file -> As described 
        # in the Python coursbook
        # Or maybe there is a better option in the csv module but I don´t know that one too well yet
        #with open (path, 'a', newline='') as update_scorebord: 

