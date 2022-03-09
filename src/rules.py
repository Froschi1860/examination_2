"""The module contains the rules of our version of the card game war."""

GAME_RULES = """
In this version of war the goal is for one player to get all the cards of the other player.

For each game a card deck of 52 cards is randomly split in half and dealt to the two players.

In each round both players draw the card on top of their hand.
The suits and values of both cards are compared and, depending on the result, the game continues
with a war or with the next draw.

A war occurs whenever either the values or the suits of both cards match.

If no war occurs, the card with the higher value wins and the winner puts both cards underneath
their stack. Then the game continues with the next draw.

If a war occurs both players add the next three cards of their decks into the pot without looking 
at them.
The next card is drawn and the winner gets all cards in the pot. In case of another war,
again the next three cards are blindly added to the pot and the game continues with the next draw.
This repeats until a draw is won.
After a war was won, the winner receives the pot and is allowed to sort the cards in it before
putting them underneath their stack.

The game ends as soon as one player runs out of cards, regardless of whether a war is ongoing."""
