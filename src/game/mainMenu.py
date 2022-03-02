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
current - Display current player
menu - Display menu
end - End the programme"""

    def __init__(self, completekey:str=None, stdin=None, player=None, stdout=None, test_mode=False, test_cmd=""):
        '''Initialise a mainMenu object and enable test_mode for cmdloop'''
        super().__init__(completekey, stdin, stdout)
        self.player = player
        self.test_mode = test_mode
        self.test_cmd = test_cmd


    def cmdloop(self):
        '''Start menu and enforce player choice at beginning in game mode'''
        if self.test_mode:
            self.onecmd(self.test_cmd)
            self.onecmd("end")
        else:
            if self.player == None:
                print("\nPlease choose or create a player to start")
                self.onecmd(line="player")
            super().cmdloop()

    def precmd(self, line: str):
        '''Assure case-insensitivity'''
        return line.lower()

    def preloop(self):
        '''Display menu when menu is entered'''
        self.onecmd("menu")

    def do_player(self, line):
        '''Open the player menu'''
        self.player = playerMenu.PlayerMenu(player=self.player).cmdloop()

    def do_game(self, line):
        '''Set up and start a new game'''
        return

    def do_highscore(self, line):
        '''Display player statistics'''
        return "highscore"

    def do_rules(self, line):
        '''Display the game rules'''
        return "rules"

    def do_current(self, line):
        '''Display current player'''
        print(f"\nCurrent player: {self.player}")

    def do_menu(self, line):
        '''Display menu'''
        print(self.menu_message)

    def do_end(self, line):
        '''End the programme'''
        return True


welcome_message = """\nWelcome to war! How about a game of cards?
------------------------------------------"""

def main():
    '''Initialize the game interface and welcome user'''
    print(welcome_message)
    MainMenu().cmdloop()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
