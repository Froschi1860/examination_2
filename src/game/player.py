class Player:   
    
    def __init__(self, player_id, last_rounds_played = 0, total_rounds_played = 0, games_played = 0, last_game_won = False, total_games_won = 0):
        '''construct player object, defaults set so that player info can be overrided as they increase their stats'''
        self.player_id = player_id
        self.last_rounds_played = last_rounds_played
        self.total_rounds_played = total_rounds_played
        self.games_played = games_played
        self.last_game_won = last_game_won
        self.total_games_won = total_games_won
    
    
    def add_player(self, player_id):
        '''add new player to a file of players, for now it is written as a list'''
        self.player_list = self.player_list.append(player_id)
        return self.player_list
    
    def play_round(self):
        '''adds a round played to the player's stats (maybe better suited for the game class)'''
        self.rounds_played += 1
        return self.rounds_played
          
    def get_total_rounds(self):
        '''adds total rounds played to the player's stats'''
        self.total_rounds += self.rounds_played
        return self.total_rounds
    
    def play_game(self):
        '''adds a game played to player's stats, again probably better in game class'''
        self.games_played += 1
        return self.games_played
    
    def get_total_games(self):
        '''add total number of games to player's stats'''
        self.total_games += self.games_played
        return self.games_played
    
    def win_game(self):
        '''show the player has won a game'''
        self.games_won += 1
        return self.games_won
    
    def get_total_wins(self):
        '''adds total number of individual wins to the player's stats'''
        self.total_wins =+ self.games_won
        return self.total_wins

def check_player_id(self, player_id, player_list):
    '''read a file of exisitng players, but for now I have it as a list'''
    if self.player_id in self.player_list:
        return True
    else: 
        return False

def change_player_id(self, new_player_id):
    '''returns a player object
    self.player_id = new_player_id
    return self.player_id'''

def choose_player(player_id):
        '''open file, player_list.txt retreive info for player use index values for constructor'''
        Player(player_id) 
        