import cmd, player


class PlayerMenu(cmd.Cmd):
    
    prompt = "\n(Player menu) "

    player = None

    menu_message = """
Player menu
------------------------------------------

Please choose one of the folowing options:

choose - Open an existing player profile
create - Create a new player profile
current - Display current Player
id - Change name of current player
menu - Display menu
exit - Return to main menu"""

    def __init__(self, completekey='tab', stdin: str=None, stdout: str=None, player=None):
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
        '''Display menu and current player when menu is entered'''
        self.onecmd(line="current")
        print(self.menu_message)

    def current_player(self):
        '''Return currrent player'''
        if self.player == None:
            return "\nNo player chosen"
        else:
            return f"\nCurrent player: {self.player}"

    def do_current(self, line):
        '''Display current player'''
        print(self.current_player())

    def do_id(self, line):
        '''Change id of current player'''
        new_player_name = input("Please enter the new id: ")
        while player.check_player_id(new_player_name):
            print("A player with the chosen id already exists")
            new_player_name = input("Please enter the new id: ")
        self.player = self.player.change_player_id(new_player_name)
        return self.player

    def do_menu(self, line):
        '''Display menu'''
        self.preloop()

    def do_choose(self, line):
        '''Open an existing player profile'''
        player_name = input("Please enter the player name: ")
        if not player.check_player_id(player_name):
            print("The chosen player does not exist")
        else:
            self.player = player.choose_player()
        self.onecmd(line="current")
    
    def do_create(self, line):
        '''Create a new player profile'''
        new_player_name = input("Please enter the name of the new player: ")
        while player.check_player_id(new_player_name):
            print("A player with this name already exists.")
            new_player_name = input("Please enter the name of the new player: ")
        self.player = player.Player(new_player_name)
        return self.player

    def do_exit(self, line):
        '''Return to main menu after player was chosen'''
        if self.player == None:
            print("\nChoose or create a player to continue")
            return self.player
        else:
            return True
