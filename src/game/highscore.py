import Player

class Highscore:
    
    format = '''HIGHSCORE RESULTS:\n
    ------------------------'''
    
    def __init__(self, player_list):
        self.player_list = player_list
    
    def sort_score_results(self):
        return sorted(self.player_list, key=lambda x: x['Total Games Won'])
  
    