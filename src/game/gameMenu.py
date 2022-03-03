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

    def __init__(self, player_1, player_2, test_mode=False, test_cmd="", setup=("pvc", "com")):
        super().__init__()
        self.player_1 = player_1
        if player_2 == None:
            self.player_2 = player.choose_player("com")
        else:
            self.player_2= player_2
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
        new_game = game.Game(player_1=self.player_1, player_2=self.player_2, difficulty=self.setup[2])
        new_game.play()

    def do_setup(self, line):
        '''Change setup: First argument game mode pvc/pvp; Second argument: Id of player 2 if pvp was chosen'''
        invalid_input_msg = "\nThe inputs of arguments was invalid. Type help setup for instructions."
        args = line.split()
        if len(args) <= 1 and args[0] == "pvc":
            self.setup = ("pvc", "com")
        elif len(args) <= 2 and args[0] == "pvp":
            player_2_id = args[1]
            # If player_2_id exists choose them otherwise create a new player and set set self.player_2
        else:
            print(invalid_input_msg)

    def do_current(self, line):
        '''Display currrent setup'''
        if self.setup[0] == "pvc":
            mode = "player vs computer"
        else:
            mode = "player vs player"
        if self.setup[1] == "com":
            player_2 = "Computer"
        else:
            player_2 = self.setup[1]
        print(f"Current setup: Game mode {mode} -> {self.player_1} plays against {player_2}")

    def do_menu(self, line):
        '''Display menu'''
        print(self.menu_message)

    def do_exit(self, line):
        '''Return to main menu'''
        return True


        