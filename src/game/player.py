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
    
    with open (path, 'a', newline='') as update_scorebord: 
        
        
    # new_stats = Player(player_id=player_id, last_rounds_played=last_rounds_played, total_rounds_played=rounds, last_game_won=last_game_won, total_games_won=games)  
    # return new_stats
      

            
        
        def change_player_id(self, new_player_id):
            '''returns a player object'''
    

    def choose_player(player_id):
        '''open file, player_list.txt retreive info for player use index values for constructor'''

        return Player(player_id)
