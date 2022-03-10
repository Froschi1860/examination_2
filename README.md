War
=================

An implementation of the card game war as command line game. (Current version: v1.0.0)  
Played games are saved in this game and a highscore of all games played since installation can be displayed.  

Game rules in this implementation:
----------------------------------

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

The game ends as soon as one player runs out of cards, regardless of whether a war is ongoing.


Requirements
--------------------

### Starting the game
* Python 3 needs to be installed
* Git Bash needs to be installed on Windows and all commands must be run in Git Bash

### Using automated commands (linting, documentation, etc.)
* Make needs to be installed
* The Python path variable needs to be set to python (or python 3 with adjustment in the Makefile)
* Graphviz needs to be installed to automatically create UML diagrams


Install the app
--------------------

The easiest way to install the app is to use git. In the command line, navigate to the folder where you would like to intall the game and run:
```
git copy https://github.com/Froschi1860/examination_2.git
```

Alternatively, go to https://github.com/Froschi1860/examination_2.git to download a zip-file with the app. Unpack this file in a directory of your choice and enter it via the command line.  


Start the game
-----------------
### Using make

Start the game by executing the command:
```
make start-game
```

### Not using make

Change into the src/ directory and run main.py:
```
# For Git bash
cd src/
python main.py
```


Navigate the ingame menus
-----------------

All menus support the command help.   
All commands are case-insensitive.  
Invalid commands are handled.  
Invalid arguments after commands are ignored if no arguments are expected, otherwise they are handled.  
Additional arguments that are not expected are ignored.  
Player IDs are case-sensitive.  

### Main menu

Type the following commands and confirm with enter to navigate:  

    player - Open the player menu
    game - Set up and start a new game
    highscore - Display player statistics
    rules - Display the game rules
    current - Display current player
    menu - Display menu
    end - End the programme

### Player menu

Type the following commands and confirm with enter to navigate (necessary arguments in angular brackets):  

    choose <player_id> - Open an existing player profile
    create <player_id> - Create a new player profile
    id <player_id> - Change id of current player
    current - Display current Player
    menu - Display menu
    exit - Return to main menu

### Game menu

Type the following commands and confirm with enter to navigate (necessary arguments in angular brackets): 

```
    start - Start a new game with current setup
    setup <mode:"pvc"/"pvp"> <only in mode pvp:"player_2_id"> - Change setup
    current - Display currrent setup
    menu - Display menu
    exit - Return to main menu
```

### Inside a game

When no war is happening:
* Press enter to draw the next cards for both players.
* Type exit and to end the current game without saving the result in the highscore.
* Restart with the same setup is possible by exiting the game and typing start in the game menu.
* Type cheat to simulate the rest of the current game. Result is saved in highscore.

After a won war:
* Type switch to change two cards. Enter index of first card, then index of second card.
* Type done once the sorting is finished.


Implementation of computer player
-----------------------------
In this version (v1.0.0) the computer is implemented to automatically handle won wars without need for user input.  
In later versions different levels of intelligence for the computer may be added.  


Run more commands
------------------
The programme setup supports different tools utilizing make  

### Check python version

To get information on the current python version type:
```
make version
```


### Start virtual environment

It is recommended to start a virtual environment (venv) before running any commands other than starting the game and checking the python version.  

To create and start a virtual environment type
```
make venv
```
and follow the instructions shown.  

### Install necessary packages

NOTE: Virtual environment should be started before.  

To install all necessary packages run:
```
make install
```

To check installed packages run:
```
make installed
```


### Static code analysis
NOTE: Install necessary packages before.  

To execute static code analysis run:
```
make lint
```

The messages displayed are known to the code authors and the goal is to solve them in future versions.  


### Unittests and code coverage
NOTE: Install necessary packages before.  
NOTE: Running the unittests and/or coverage will delete the saved player statistics.  

To execute the test suites and create coverage reports run:
```
make test
```

The coverage reports are saved in the directory htmlcov/  

Code coverage of more than 90% for each module was the internal goal for this version.  

A decision was taken not to include test suites for main.py and rules.py. All functionality in main.py is covered in the other test suites and rules.py contains only a description of the game rules.  


### Documentation and UML
NOTE: Install necessary packages before.  

To create documentation run:
```
make doc
```

The results are saved in the directory doc/.  

Documentation is created using pdoc and UML diagrams using pyreverse and graphviz.  


### Code metrics
NOTE: Install necessary packages before.  

To create code metrics run:
```
make metrics
```

The results are displayed in the terminal.  


### Removing created files
NOTE: This step should be executed after running any command except starting the game.  

To remove all created files run:
```
make clean-doc
```

To remove all created files and the virtual environment run:
```
make clean-all
```


Code authors:
-------------------
* Enzo Tiberghien
* Fabian Fröschl
* Wibecka Oliver

All code was developed in a collaborative manner.  

The project structure and Makefile were created using the template at https://gitlab.com/mikael-roos/python-template/-/tree/main.