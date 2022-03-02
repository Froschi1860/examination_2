class Player:
    def __init__(self, name="Fabi"):
        self.name = name

def main():
    player_1 = Player()
    print(player_1.name)
    player_2 = Player("Vee")
    print(player_2.name)

if __name__ == "__main__":
    main()