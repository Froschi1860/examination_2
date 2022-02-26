import cmd, playerMenu, highscore


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
current - Display current player
menu - Display menu
end - End the programme"""

    player = None

    def cmdloop(self):
        '''Start menu and enforce player choice at beginning'''
        if self.player == None:
            print("\nPlease choose or create a player to start")
            self.onecmd(line="player")
        super().cmdloop()

    def preloop(self):
        '''Display menu and current player when menu is entered'''
        self.onecmd(line="current")
        print(self.menu_message)

    def do_menu(self, line):
        '''Display menu'''
        self.preloop()

    def do_player(self, line):
        '''Open the player menu'''
        self.player = playerMenu.PlayerMenu(player=self.player).cmdloop()#[1]

    def current_player(self):
        '''Return current player'''
        return f"\nCurrent player: {self.player}"

    def do_current(self, line):
        '''Display current player'''
        print(self.current_player())

    def do_game(self, line):
        '''Set up and start a new game'''
        return "game"

    def do_highscore(self, line):
        '''Display player statistics'''
        return "highscore"

    def do_rules(self, line):
        '''Display the game rules'''
        return "rules"

    def do_end(self, line):
        '''End the programme'''
        return True

welcome_message = """\nWelcome to war! How about a game of cards?
------------------------------------------"""

def start_cli():
    '''Initialize the game interface and welcome user'''
    print(welcome_message)
    MainMenu().cmdloop()

if __name__ == "__main__":
    start_cli()
