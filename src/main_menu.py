'''The module contains a class that creates and initialises the main menu for war.
A test mode is availabe for unit tests.
In game mode the user is initialy redirected to the player menu to enforce player choice.'''

import cmd
import player_menu
import game_menu
import highscore
import player
import rules


class MainMenu(cmd.Cmd):
    '''This class provides functionality for the main menu.

The menu is displayed when entered.

Case-insensitivity is ensured.

Commands:
player - Open the player menu
game - Set up and start a new game
highscore - Display player statistics
rules - Display the game rules
current - Display current player
menu - Display menu
end - End the programme

Command help <command> is available.
'''

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

    def __init__(self, player_1=None, player_2=None, test_mode=False, test_cmd=""):
        '''Initialise a mainMenu object and enable test_mode for cmdloop'''
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.test_mode = test_mode
        self.test_cmd = test_cmd
        self.setup = None
        self.game_rules = rules.game_rules

    def cmdloop(self, intro=None):
        '''Run menu and enforce player choice at beginning in game mode'''
        if self.test_mode:
            self.onecmd(self.test_cmd)
            self.onecmd("end")
        else:
            if self.player_1 is None:
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
        line.strip()
        if not self.test_mode: # Start player menu
            self.player_1 = player_menu.PlayerMenu(player_1=self.player_1).cmdloop()
        else:
            print("Player menu entered")

    def do_game(self, line):
        '''Set up and start a new game'''
        line.strip()
        if not self.test_mode: # Start game menu
            self.setup, self.player_2 = game_menu.GameMenu(player_1=self.player_1,
                player_2=self.player_2, setup=self.setup).cmdloop()
        else:
            print("Game menu entered")

    def do_highscore(self, line):
        '''Display player statistics'''
        line.strip()
        highscore.Highscore(player.player_list).display_highscore()

    def do_rules(self, line):
        '''Display the game rules'''
        line.strip()
        print(self.game_rules)

    def do_current(self, line):
        '''Display current player'''
        line.strip()
        print(f"\nCurrent player: {self.player_1}")

    def do_menu(self, line):
        '''Display menu'''
        line.strip()
        print(self.menu_message)

    def do_end(self, line):
        '''End the programme'''
        line.strip()
        if self.test_mode:
            print("Ending")
        return True
