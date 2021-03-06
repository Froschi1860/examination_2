"""The module contains a class to creates and initialises the player sub-menu.

A test mode is availabe for unit tests.
To leave the sub-menu ingame mode a player must be chosen.
"""

import cmd
import player


class PlayerMenu(cmd.Cmd):
    """This class provides functionality for the sub-menu player.

    The menu is displayed when entered.

    Case-insensitivity is ensured.

    Commands:
    choose <player_id> - Open an existing player profile
    create <player_id> - Create a new player profile
    id <player_id> - Change id of current player
    current - Display current Player
    menu - Display menu
    exit - Return to main menu

    Command help <command> is available.
    """

    prompt = "\n(Player menu) "

    menu_message = """
Player menu
------------------------------------------

Please choose one of the folowing options:

choose <player_id> - Open an existing player profile
create <player_id> - Create a new player profile
id <player_id> - Change id of current player
current - Display current Player
menu - Display menu
exit - Return to main menu"""

    def __init__(self, player_1=None, test_mode=False, test_cmd=""):
        """Initialise a PlayerMenu object and enable test mode."""
        super().__init__()
        self.player_1 = player_1
        self.test_mode = test_mode
        self.test_cmd = test_cmd

    def cmdloop(self, intro=None):
        """Run menu and return current player in game mode."""
        if self.test_mode:
            self.onecmd(self.test_cmd)
            self.onecmd("exit")
        else:
            super().cmdloop()
        return self.player_1

    def precmd(self, line: str):
        """Assure case-insensitivity."""
        return line.lower()

    def preloop(self):
        """Display menu when menu is entered."""
        if self.player_1 is None:
            print("\nPlease choose or create a player to start")
        self.onecmd("menu")

    def do_choose(self, line):
        """Open an existing player profile and display chosen player."""
        player_id = line
        if player_id == "":
            print("Enter a player id to choose a player: choose <player_id>")
        elif player_id == "com":
            print("The computer can not be chosen as player")
        elif not player.check_player_id(player_id):
            print(f"The player with the id {player_id} does not exist")
        else:
            self.player_1 = player.choose_player(player_id)

    def do_create(self, line):
        """Create a new player profile."""
        args = line.split()
        if len(args) == 1 and player.check_player_id(args[0]):
            print(f"A player with the id {args[0]} already exists.")
        elif len(args) == 1 and not player.check_player_id(args[0]):
            self.player_1 = player.Player(args[0])
            player.add_player(args[0])
        else:
            print("Enter a player id to create a player: create <player_id>")

    def do_id(self, line):
        """Change id of current player."""
        new_player_id = line
        if new_player_id == "":
            print("Enter a player id to change the id of the current " +
                  "player: id <player_id>")
        elif self.player_1 is None:
            print("Choose or create a player before changing the id")
        elif player.check_player_id(new_player_id):
            print(f"A player with the id {new_player_id} already exists")
        else:
            self.player_1.change_player_id(new_player_id)

    def do_current(self, line):
        """Display current player."""
        line.strip()
        if self.player_1 is None:
            print("\nNo player chosen")
        else:
            print(f"\nCurrent player: {self.player_1}")

    def do_menu(self, line):
        """Display menu."""
        line.strip()
        print(self.menu_message)

    def do_exit(self, line):
        """Return to main menu after player was chosen."""
        line.strip()
        if not self.test_mode:
            if self.player_1 is not None:
                return True
            print("\nChoose or create a player to continue")
            return None
        print("Exiting")
        return True
