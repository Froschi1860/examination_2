#!/usr/bin/env make

# Change this to be your variant of the python command
# Set the env variable PYTHON to another value if needed
# PYTHON=python3 make version
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:


# ---------------------------------------------------------
# Check the current python executable.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.
#
venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc src/.coverage
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc/pyreverse doc/pdoc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


# ---------------------------------------------------------
# Work with static code linters.
#
# Works, nut shows import errrors
pylint:
	@$(call MESSAGE,$@)
	-cd src/ && $(PYTHON) -m pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-cd src/ && flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	cd src/ && $(PYTHON) -m unittest discover

coverage:
	@$(call MESSAGE,$@)
	-cd src/ && coverage run -m unittest discover
	cd src/ && coverage html
	cd src/ && coverage report -m
	mv src/htmlcov/ .
	rm src/.coverage

test: unittest coverage


# ---------------------------------------------------------
# Work with generating documentation.
#

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/pdoc src/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse src/*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse


# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average src

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show src

radon-raw:
	@$(call MESSAGE,$@)
	radon raw src

radon-hal:
	@$(call MESSAGE,$@)
	radon hal src

# Does not yet work -> When working, include in target metrics
cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory src

metrics: radon-cc radon-mi radon-raw radon-hal


# ---------------------------------------------------------
# Start the game war
#
start-game:
	@$(call MESSAGE,$@)
	cd src/ && $(PYTHON) main.py
