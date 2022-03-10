"""The module contains a class that creates and initialises the highscore.

A test mode is availabe for unit tests.
"""

class Highscore:
    """This class creates, reads and displays the Highscore."""

    def __init__(self, player_list):
        """Intitalize the player list in the highscore object."""
        self.player_list = player_list


    def sort_score_results(self):
        """Sorts the highscore based on which player has acheived the most
        wins and truncates the scoreboard to only show the desired statistics
        for each player.
        """
        scoreboard = []
        ranked_list_of_dicts = sorted(self.player_list,key=lambda player: player['Total Games Won'], 
                                      reverse = True)
        for player in ranked_list_of_dicts:
            stats = player.values()
            player_stats = list(stats)
            scoreboard.append(player_stats[0:4])

        return scoreboard

    def display_highscore(self):
        """Displays the highscore according to a particular format."""
        header = '''
HIGHSCORE RESULTS:\n
---------------------------------------------------------------------\n
PLAYER        | TOTAL WINS | TOTAL GAMES PLAYED | TOTAL ROUNDS PLAYED 
---------------------------------------------------------------------'''
        print(header)
        scoreboard = self.sort_score_results()
        for player in scoreboard:
            print(f'{player[0]:<15}{player[1]:<13}{player[2]:<22}{player[3]:<21}')

        