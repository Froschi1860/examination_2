

class player:   
    
    player_list = []
    
    def __init__(self, player_id,):
        '''construct player object'''
        self.player_id = player_id
        self.rounds_played = 0
        self.total_rounds = 0
        self.games_played =0
        self.total_games = 0
        self.games_won = 0 
        self.total_wins = 0
    
    def set_player_list(self, player_list):
        '''assign player list, will maybe be replaces by file'''
        self.player_list = player_list
    
    def check_player_id(self, player_id, player_list):
        '''read a file of exisitng players, but for now I have it as a list'''
        if self.player_id in self.player_list:
            return "Welcome back {self.player_id}!"
        else: 
            return "Welcome new player {self.player_id}!"
    
    def add_player(self, player_id):
        '''add new player to a file of players, for now it is written as a list'''
        self.player_list = self.player_list.append(player_id)
        return self.player_list
    
    def change_player_id(self, new_player_id):
        '''allow a player to change their name'''
        self.player_id = new_player_id
        return new_player_id
    
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
    