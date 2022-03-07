import cmd, playerMenu, gameMenu, highscore, player, rules


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

    def __init__(self, player_1=None, player_2=None, test_mode=False, test_cmd="", setup=("pvc", "com")):
        '''Initialise a mainMenu object and enable test_mode for cmdloop'''
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.test_mode = test_mode
        self.test_cmd = test_cmd
        self.setup = setup

    def cmdloop(self):
        '''Run menu and enforce player choice at beginning in game mode'''
        if self.test_mode:
            self.onecmd(self.test_cmd)
            self.onecmd("end")
        else:
            if self.player_1 == None:
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
        if self.test_mode:
            return playerMenu.PlayerMenu()
        else:
            self.player_1 = playerMenu.PlayerMenu(player_1=self.player_1).cmdloop()

    def do_game(self, line):
        '''Set up and start a new game'''
        if self.test_mode:
            return gameMenu.GameMenu(player_1=self.player_1)
        else:
            game_menu = gameMenu.GameMenu(player_1=self.player_1, player_2=self.player_2, setup=self.setup)
            self.setup, self.player_2 = game_menu.cmdloop()

    def do_highscore(self, line):
        '''Display player statistics'''
        if self.test_mode:
            return highscore.Highscore(player.player_list)
        else:
            highscore.Highscore(player.player_list).display_highscore()

    def do_rules(self, line):
        '''Display the game rules'''
        print(rules.game_rules)

    def do_current(self, line):
        '''Display current player'''
        print(f"\nCurrent player: {self.player_1}")

    def do_menu(self, line):
        '''Display menu'''
        print(self.menu_message)

    def do_end(self, line):
        '''End the programme'''
        return True


welcome_message = """\nWelcome to war! How about a game of cards?
------------------------------------------"""

def main():
    '''Initialize the programe by loading or initialising player data and welcome user'''
    print(welcome_message)
    player.player_list = player.read_player_data()
    if not player.check_player_id("com"):
        player.add_player(player.Player("com").player_id)
    MainMenu().cmdloop()
    player.write_player_data(player.player_list)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
