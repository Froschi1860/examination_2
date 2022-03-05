
import player

class Highscore:
    
    
    def __init__(self, player_list):
        self.player_list = player_list
    
    def sort_score_results(self):
        scoreboard = []
        ranked_list_of_dicts = sorted(self.player_list, key=lambda player: player['Total Games Won'])
        for player in ranked_list_of_dicts:
            stats = player.values()
            player_stats = list(stats)
        
        for list_player in player_stats:
            scoreboard.append(list_player)
        
        return scoreboard

    def display_highscore(self):
        header = '''HIGHSCORE RESULTS:\n
                    ------------------------\n
                    PLAYER    | TOTAL WINS | TOTAL GAMES PLAYED | TOTAL ROUNDS PLAYED 
                    ------------------------------------------------------------------'''
        print(header)
        scoreboard = self.sort_score_results()
        for player in scoreboard:
            return f'{player[0:4]}'
