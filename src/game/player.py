'''This class constructs a player and adds them to a list of dictionaries which contains information about each player object.
This allows the user to select a player, make a new player, or even change the name of their already saved player'''

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
        self.add_player()


    def add_player(self):
        '''adds a player to the player stats file/list'''
        player_stats = {'Player ID': self.player_id,'Total Games Won': self.total_games_won, 
                        'Total Games Played' :self.games_played, 'Total Rounds Played': self.total_rounds_played, 
                        'Last Game Won': False, 'Last Rounds Played': self.last_rounds_played}
        player_list.append(player_stats)

    
    def change_player_id(self,new_player_id):
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
        return f"{self.player_id}"


def choose_player(player_id):
    for player in player_list:
        if player['Player ID'] == player_id:
                selected_player = Player(player_id=player_id, last_rounds_played = player['Last Rounds Played'], 
                total_rounds_played=player['Total Rounds Played'], games_played=player['Total Games Played'],
                last_game_won=False, total_games_won= player['Total Games Won'])
                selected_player.add_player()
                return selected_player

def check_player_id(player_id):
    '''checks to see if the player already has stats'''
    return_value = False
    for player in player_list:
        if player['Player ID'] == player_id:
            return_value = True
    return return_value 