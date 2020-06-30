#!/usr/bin/env python3
import json
import argparse
import os
import sys
from assets.PP import PPrint  # Pretty printing

# Argument parsing
parser = argparse.ArgumentParser(
    description='''Standalone quiz application generator. Functions both interactivly or with args. ''')
parser.add_argument("--foo", type=int, default=42, help="FOO!")
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
args = parser.parse_args()


def LogoPrint():
    print(
        """
___________              __  ________        .__         ________
\\__    ___/___ ___  ____/  |_\\_____  \\  __ __|__|_______/  _____/  ____   ____
  |    |_/ __ \\\  \\/  /\\   __\\/  / \\  \\|  |  \\  \\___   /   \\  ____/ __ \\ /    \\
  |    |\\  ___/ >    <  |  | /   \\_/.  \  |  /  |/    /\\    \\_\\  \\  ___/|   |  \\
  |____| \\___  >__/\\_ \\ |__| \\_____\\ \\_/____/|__/_____ \\\______  /\\___  >___|  /
             \\/      \\/             \\__>              \\/       \\/     \\/     \\/
================================================================================
"""
    )


# MAIN APPLICATION
print('\x1b[2J')  # clear screen
LogoPrint()
PPrint("No options given, assuming interactive mode.", "info")
# First generate json
PPrint("Preparing to generate JSON...", "info")
try:
    from assets.jsonbuilder import QuestionGen, BuildJSON
    BuildJSON("temp_questions.json")
except Exception as e:
    PPrint("JSON Building failed! Erroring out...", "minus")
    PPrint("Exception: " + str(e), "minus")
    sys.exit(1)
print("\n")
PPrint("Temporary JSON successfully created!", "plus")

# Do some extra things to it? e.g scramble, obfuscate
try:
    from assets.operations import shuffle
    PPrint("What shuffle mode? (N)one, (A)nswers, (Q)uestions, or (B)oth?", "module")
    PPrint("Both is default if no input. Lowercase and uppercase accepted.", "module")
    shuffleMode = input("")
    if shuffleMode.upper() == "" or shuffleMode.upper()[0] == "B":
        shuffle("temp_questions.json").both()
        PPrint("Shuffling completed.", "plus")
    elif shuffleMode.upper()[0] == "A":
        shuffle("temp_questions.json").answers()
        PPrint("Shuffling completed.", "plus")
    elif shuffleMode.upper()[0] == "Q":
        shuffle("temp_questions.json").questions()
        PPrint("Shuffling completed.", "plus")
    else:
        pass
    # dont want to print shuffling completed if none asked for
except Exception as e:
    PPrint("Shuffling failed! Attempting to carry on...", "minus")
    PPrint("Exception: " + str(e), "minus")

# Then build application as .pyc
PPrint("Preparing to build application...", "info")
PPrint("Quiz filename? (No extension - .pyc will get generated)", "module")
name = input("")
try:
    from assets.pybuilder import PyBuilder
    filename = PyBuilder().build(name)
except Exception as e:
    PPrint(".py Building failed! Erroring out...", "minus")
    PPrint("Exception: " + str(e), "minus")
    sys.exit(1)
PPrint("base .py file created.", "plus")
try:
    import py_compile
    py_compile.compile(filename, filename.replace(".py", ".pyc"))
except Exception as e:
    PPrint(".pyc Building failed! Erroring out...", "minus")
    PPrint("Exception: " + str(e), "minus")
    sys.exit(1)
# print("\n")
PPrint(".pyc file created!", "plus")
PPrint("Removing bare .py file...", "info")
os.remove(filename)
PPrint("Quiz creation completed with no errors!", "plus")
sys.exit(0)
