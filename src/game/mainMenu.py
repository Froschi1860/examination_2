import cmd, playerMenu


class MainMenu(cmd.Cmd):

    prompt = "\n(Main menu) "

    menu_message = """
Main menu
------------------------------------------

Please choose one of the folowing options:

player - Open the player menu
game - Set up and start a new game
highscore - Display player statistics
rules - Display the game rules
chosen - Display current player
exit - End the programme"""

    player = None

    def cmdloop(self):
        '''Start menu and enforce player choice at beginning'''
        if self.player == None:
            print("\nPlease choose or create a player to continue")
            self.onecmd(line="player")
        return super().cmdloop()

    def preloop(self):
        '''Display menu and current player when menu is entered'''
        self.onecmd(line="chosen")
        print(self.menu_message)

    def do_menu(self, line):
        '''Display menu'''
        self.preloop()

    def do_player(self, line):
        '''Open the player menu'''
        self.player = playerMenu.PlayerMenu().cmdloop()[1]

    def chosen_player(self):
        '''Return chosen player'''
        return f"\nCurrent player: {self.player}"

    def do_chosen(self, line):
        '''Display chosen player'''
        print(self.chosen_player())

    def do_game(self, line):
        '''Set up and start a new game'''
        return "game"

    def do_highscore(self, line):
        '''Display player statistics'''
        return "highscore"

    def do_rules(self, line):
        '''Display the game rules'''
        return "rules"

    def do_exit(self, line):
        '''End the programme'''
        return True
