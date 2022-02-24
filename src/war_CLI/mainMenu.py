import cmd, playerMenu


class MainMenu(cmd.Cmd):

    prompt = "(Main menu) "

    display_menu = """Main menu
------------------------------------------

Please choose one of the folowing options:

player - Open the player menu
game - Set up and start a new game
highscore - Display player statistics
rules - Display the game rules
exit - End the programme
"""

    def cmdloop(self, intro=display_menu):
        '''Display menu when it is entered first time'''
        return super().cmdloop(intro)

    def preloop(self):
        '''Altering layout'''
        print()

    def do_player(self, line):
        '''Open the player menu'''
        playerMenu.PlayerMenu().cmdloop()
    
    def do_game(self, line):
        '''Set up and start a new game'''

    def do_highscore(self, line):
        '''Display player statistics'''

    def do_rules(self, line):
        '''Display the game rules'''

    def do_exit(self, line):
        '''End the programme'''
        return True
