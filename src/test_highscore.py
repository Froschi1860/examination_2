import unittest
import highscore

class testHighscore(unittest.TestCase):
    
    def setUp(self):
        self.mock_player_list = ([
            {'Player ID': "test player 1", 'Total Games Won': 0,
            'Total Games Played': 1 , 'Total Rounds Played': 0, 
            'Last Game Won': True, 'Last Rounds Played': 0 }, 
            
            {'Player ID':"test player 2" ,'Total Games Won': 1,
            'Total Games Played': 0 , 'Total Rounds Played': 0, 
            'Last Game Won': False, 'Last Rounds Played': 0 }
            ])
        
# test initializer  
    def test_init_function(self):
        test_highscore = highscore.Highscore(self.mock_player_list)
        self.assertIsInstance(test_highscore, highscore.Highscore)
    
    def test_sort_score_results_by_winner(self):
        
        test_highscore = highscore.Highscore(self.mock_player_list)
        test_scoreboard = test_highscore.sort_score_results
        self.assertTrue(test_scoreboard, len(test_scoreboard) == 4)
        
        
        
  
    
#     def sort_score_results(self):
#         '''sorts the highscore based on which player has acheived the most wins and truncates the scoreboard to 
#         only show the desired statistics for each player'''
#         scoreboard = []
#         ranked_list_of_dicts = sorted(self.player_list, key=lambda player: player['Total Games Won'], reverse = True)
#         for player in ranked_list_of_dicts:
#             stats = player.values()
#             player_stats = list(stats)
#             scoreboard.append(player_stats[0:4])
        
#         return scoreboard

#     def display_highscore(self):
#         '''displays the highscore according to a particular format'''
        
#         header = '''
# HIGHSCORE RESULTS:\n
# ---------------------------------------------------------------------\n
# PLAYER        | TOTAL WINS | TOTAL GAMES PLAYED | TOTAL ROUNDS PLAYED 
# ---------------------------------------------------------------------'''
#         print(header)
#         scoreboard = self.sort_score_results()
#         for player in scoreboard:
#             print(f'{player[0]:<15}{player[1]:<13}{player[2]:<22}{player[3]:<21}')

if __name__ == '__main__':
    unittest.main()