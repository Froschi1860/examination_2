import cmd
import mainMenu


class WarCLI(cmd.Cmd):
    '''Start the game interface'''

    def cmdloop(self):
        '''Start main menu'''
        return mainMenu.MainMenu().cmdloop()

welcome_message = """\nWelcome to war! How about a game of cards?
------------------------------------------"""

def start_cli():
    '''Initialize the game interface and welcome user'''
    print(welcome_message)
    WarCLI().cmdloop()

if __name__ == "__main__":
    start_cli()