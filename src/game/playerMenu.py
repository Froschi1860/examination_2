import cmd, player
from encodings import normalize_encoding


class PlayerMenu(cmd.Cmd):
    
    prompt = "\n(Player menu) "

    player = None

    menu_message = """
Player menu
------------------------------------------

Please choose one of the folowing options:

choose - Open an existing player profile
create - Create a new player profile
id - Change id of current player
current - Display current Player
menu - Display menu
exit - Return to main menu"""

    def __init__(self, completekey='tab', stdin: str=None, stdout: str=None, player: player=None):
        '''Initialise a PlayerMenu object and sets self.player is a player is already chosen'''
        super().__init__(completekey, stdin, stdout)
        self.player = player

    def cmdloop(self):
        '''Run menu and return current player'''
        super().cmdloop()
        return self.player

    def precmd(self, line: str):
        '''Assure case-insensitivity'''
        return line.lower()

    def preloop(self):
        '''Display menu when menu is entered'''
        self.onecmd("menu")

    def do_choose(self, line):
        '''Open an existing player profile and display chosen player'''
        player_id = input("Please enter the player id: ")
        if not player.check_player_id(player_id):
            print("The chosen player does not exist")
        else:
            self.player = player.choose_player()
        self.onecmd(line="current")

    def do_create(self, line):
        '''Create a new player profile'''
        new_player_id = input("Please enter the id of the new player: ")
        if player.check_player_id(new_player_id):
            print("A player with this id already exists.")
        else:
            self.player = player.Player(new_player_id)
        self.onecmd(line="current")

    def do_id(self, line):
        '''Change id of current player'''
        new_player_id = input("Please enter the new id: ")
        if player.check_player_id(new_player_id):
            print("A player with the chosen id already exists")
        else:
            self.player = player.change_player_id(new_player_id)
        self.onecmd(line="current")

    def do_current(self, line):
        '''Display current player'''
        if self.player == None:
            print("\nNo player chosen")
        else:
            print(f"\nCurrent player: {self.player}")

    def do_menu(self, line):
        '''Display menu'''
        print(self.menu_message)

    def do_exit(self, line):
        '''Return to main menu after player was chosen'''
        if self.player == None:
            print("\nChoose or create a player to continue")
        else:
            return True
