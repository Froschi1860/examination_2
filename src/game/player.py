import csv
from csv import DictWriter

# def createfile():
#     '''Create Player_Stats CSV file that we can work with'''
#     filename = 'Player_stats.csv'
#     header = ['Player ID', 'Total Wins', 'Total Games Played', 'Total Rounds Played' ]
#     with open (filename, 'w') as file: 
#         writer = csv.writer(file)
#         writer.writerow(header)
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


    def check_player_id(self, player_id):
        '''checks to see if the player already has stats'''
        for player in player_list:
            for val in player:
                if val == player_id:
                    return True
                else:
                    return False
        # with open(path, 'r') as file:
        #     reader = csv.reader(file, delimiter=",")
        #     for row in reader:
        #         if player_id == row[0]:
        #             return True 
        #         else:
        #             return False 

    def add_player(self, player_id):
        '''adds a player to the player stats file/list'''
        player_stats = {'Player ID': player_id,'Total Games Won': self.total_games_won, 
                        'Total Games Played' :self.games_played, 'Total Rounds Played': self.total_rounds_played, 
                        'Last Game Won': False, 'Last Rounds Played': self.last_rounds_played}
        player_list.append(player_stats)
        # with open(path, 'a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(player_stats)
        #     file.close()

    def update_player_stats(self, player_id): 
        '''update player object as well as the player dictionary in the list'''
        if self.last_game_won == True:
            add_game = 1
        else:
            add_game = 0
               
        for player in player_list:
            for val in player:
                if val == player_id:
                    self.last_game_won = False
                    self.games_played =+ 1
                    self.total_rounds_played += self.last_rounds_played
                    player['Total Games Played'] = self.games_played 
                    player['Total Rounds Played'] += self.total_rounds_played
                    player['Total Games Won'] += add_game
                    player['Last Game Won'] = self.last_game_won
                    self.last_rounds_played = 0 
                    player['Last Rounds Played'] = self.last_rounds_played
    
    
        # with open(path, 'r') as scoreboard: 
        #     dict_reader = csv.DictReader(scoreboard)
        #     for row in dict_reader:
        #         if player_id == row['Player ID']:
        #             wins = int(row['Total Wins']) 
        #             games = int(row['Total Games Played'])
        #             rounds = int(row['Total Rounds Played'])
   

def choose_player(player_id):
    for player in player_list:
            for val in player:
                if val == player_id:
                    Player(player_id=player_id, last_rounds_played = player['Last Rounds Played'],    )
    return Player(player_id)