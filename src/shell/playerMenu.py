import cmd


class PlayerMenu(cmd.Cmd):
    
    prompt = "(Player menu) "

    display_menu = """Player menu
------------------------------------------

Please choose one of the folowing options:

choose - Open an existing player profile
create - Create a new player profile
change - Change current player profile
exit - Return to prior menu
"""

    def cmdloop(self, intro=display_menu):
        '''Display menu when it is entered first time'''
        return super().cmdloop(intro)

    def preloop(self):
        '''Altering layout'''
        print()

    def postloop(self):
        '''Altering layout'''
        print()

    def do_choose(self, line):
        '''Open an existing player profile'''
    
    def do_create(self, line):
        '''Create a new player profile'''

    def do_change(self, line):
        '''Change current player profile'''

    def do_exit(sef, line):
        '''Return to prior menu'''
        return True
