War
=================

An implementation of the card game war as command line game. (Current version: v1.0.0)



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

All menus support the command help

### Main menu



### Player menu


### Game menu


### Inside a game


Implementation of computer player
-----------------------------

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

To execute the test suites and create coverage reports run:
```
make test
```

The coverage reports are saved in the directory htmlcov/

Code coverage of more than 80% for each module was the internal goal for this version.

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