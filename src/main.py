import time, cardHand, deck, game, player
 
game = game.Game(player.Player("User"), player.Player("com"))
game.start()