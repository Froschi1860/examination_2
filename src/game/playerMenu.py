import cmd
from socket import inet_aton
from tkinter import Menu


class PlayerMenu(cmd.Cmd):
    
    prompt = "\n(Player menu) "

    menu_message = """
Player menu
------------------------------------------

Please choose one of the folowing options:

choose - Open an existing player profile
create - Create a new player profile
change - Change current player profile
chosen - Display chosen Player
exit - Return to main menu"""

    player = None

    def cmdloop(self):
        '''Run menu and return chosen player'''
        return super().cmdloop(), self.player

    def preloop(self):
        '''Display menu and chosen player when menu is entered'''
        self.onecmd(line="chosen")
        print(self.menu_message)

    def chosen_player(self):
        '''Return chosen player'''
        if self.player == None:
            return "\nNo player chosen"
        else:
            return f"\nChosen player: {self.player}"

    def do_chosen(self, line):
        '''Display chosen player'''
        print(self.chosen_player())

    def do_menu(self, line):
        '''Display menu'''
        self.preloop()

    def do_choose(self, line):
        '''Open an existing player profile'''
        self.player = "test"
        self.onecmd(line="chosen")
    
    def do_create(self, line):
        '''Create a new player profile'''

    def do_change(self, line):
        '''Change current player profile'''
        self.player = None
        self.onecmd(line="choose")

    def do_exit(self, line):
        '''Return to main menu'''
        if self.player == None:
            print("\nChoose or create a player to continue")
            return
        else:
            return True
