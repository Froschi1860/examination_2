import cmd, player


class PlayerMenu(cmd.Cmd):
    
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

    def __init__(self, completekey='tab', stdin=None, stdout=None, player: player=None, test_mode=False, test_cmd=""):
        '''Initialise a PlayerMenu object and enable test mode for cmdloop()'''
        super().__init__(completekey, stdin, stdout)
        self.player = player
        self.test_mode = test_mode
        self.test_cmd = test_cmd

    def cmdloop(self):
        '''Run menu and return current player in game mode'''
        if self.test_mode:
            self.onecmd(self.test_cmd)
            self.onecmd("exit")
        else:
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
        player_id = line
        if player_id == "":
            print("Enter a player id to choose a player: choose <player_id>")
        elif not player.check_player_id(player_id):
            print(f"The player with the id {player_id} does not exist")
        else:
            self.player = player.choose_player(player_id)

    def do_create(self, line):
        '''Create a new player profile'''
        new_player_id = line
        if new_player_id == "":
            print("Enter a player id to create a player: create <player_id>")
        elif player.check_player_id(new_player_id):
            print(f"A player with the id {new_player_id} already exists.")
        else:
            self.player = player.Player(new_player_id)

    def do_id(self, line):
        '''Change id of current player'''
        new_player_id = line
        if new_player_id == "":
            print("Enter a player id to change the id of the current player: id <player_id>")
        elif self.player == None:
            print("Choose or create a player before changing the id")
        elif player.check_player_id(new_player_id):
            print(f"A player with the id {new_player_id} already exists")
        else:
            self.player = player.change_player_id(new_player_id)

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

    def do_test(self, line):
        print(line)
