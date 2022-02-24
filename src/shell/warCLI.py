import cmd
import mainMenu


class WarCLI(cmd.Cmd):
    welcome_message = """
Welcome to war! How about a game of cards?
------------------------------------------"""

    def cmdloop(self, intro=welcome_message):
        print(intro)
        return mainMenu.MainMenu().cmdloop()


def main():
    WarCLI().cmdloop()

if __name__ == "__main__":
    main()