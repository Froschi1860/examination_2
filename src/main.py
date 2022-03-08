import mainMenu, player
 

welcome_message = """\nWelcome to war! How about a game of cards?
------------------------------------------"""

def main():
    '''Initialize the programe by loading or initialising player data and welcome user'''
    print(welcome_message)
    player.player_list = player.read_player_data()
    if not player.check_player_id("com"):
        player.add_player(player.Player("com").player_id)
    mainMenu.MainMenu().cmdloop()
    player.write_player_data(player.player_list)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
