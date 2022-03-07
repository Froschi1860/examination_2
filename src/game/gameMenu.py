import cmd, game, player


class GameMenu(cmd.Cmd):

    prompt = "\n(Game menu) "

    menu_message = """
Game menu
------------------------------------------

Please choose one of the folowing options:

start - Start a new game with current setup
setup <mode:"pvc"/"pvp"> <only mode pvp:"player_2_id"> - Change setup
current - Display currrent setup
menu - Display menu
exit - Return to main menu"""

    def __init__(self, player_1: player, player_2 : player=None, setup=("pvc", "com"), test_mode=False, test_cmd=""):
        super().__init__()
        self.player_1 = player_1 
        if player_2 == None:
            self.player_2 = player.choose_player("com")
        else:
            self.player_2 = player_2
        self.test_mode = test_mode
        self.test_cmd = test_cmd
        self.setup = setup
    
    def cmdloop(self):
        '''Run menu and return setup to main menu'''
        if self.test_mode:
            self.onecmd(self.test_cmd)
            self.onecmd("exit")
        else:
            super().cmdloop()
            return self.setup, self.player_2
    
    def precmd(self, line: str):
        '''Assure case-insensitivity'''
        return line.lower()

    def preloop(self):
        '''Display menu when menu is entered'''
        self.onecmd("menu")

    def do_start(self, line):
        '''Start a new game with current setup'''
        new_game = game.Game(player_1=self.player_1, player_2=self.player_2)
        if self.test_mode:
            print("Game started")
            return new_game
        else:
            new_game.start()

    def do_setup(self, line):
        '''Change setup: First argument game mode pvc/pvp; Second argument: Id of player 2 if pvp was chosen'''
        invalid_input_msg = "\nThe inputs of arguments was invalid. Type help setup for instructions."
        args = line.split()
        if len(args) >= 1 and args[0] == "pvc":
            self.setup = ("pvc", "com")
            self.player_2 = player.choose_player("com")
        elif len(args) >= 2 and args[0] == "pvp":
            player_2_id = args[1]
            if player.check_player_id(player_2_id):
                self.player_2 = player.choose_player(player_2_id)
                print(f"Player 2 was set to {self.player_2}")
            else:
                self.player_2 = player.Player(player_id=player_2_id)
                player.add_player(player_2_id)
                print(f"Player {self.player_2} was created and set to player 2")
            self.setup = ("pvp", player_2_id)
        else:
            print(invalid_input_msg)

    def do_current(self, line):
        '''Display currrent setup'''
        if self.setup[0] == "pvc":
            mode = "player vs computer"
        else:
            mode = "player vs player"
        print(f"Current setup: Game mode {mode} -> {self.player_1} plays against {self.setup[1]}")

    def do_menu(self, line):
        '''Display menu'''
        print(self.menu_message)

    def do_exit(self, line):
        '''Return to main menu'''
        if self.test_mode:
            print("Exiting")
            return True
        else:
            return True
