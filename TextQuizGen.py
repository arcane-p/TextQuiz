#!/usr/bin/env python3
import json
import argparse
from assets.PP import PPrint #Pretty printing

#Argument parsing
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
=================================================================================
"""
    )


#MAIN APPLICATION
print('\x1b[2J') # clear screen
LogoPrint()
PPrint("No options given, assuming interactive mode.", "info")
#First generate json
PPrint("Preparing to generate JSON...", "info")
try:
    from assets.jsonbuilder import QuestionGen, BuildJSON
    BuildJSON("temp_questions.json")
except Exception as e:
    PPrint("JSON Building failed! Erroring out...", "minus")
    PPrint("Exception: " + str(e), "minus")
    exit(0)
print("\n")
PPrint("Temporary JSON successfully created!", "plus")

#Do some extra things to it? e.g scramble, obfuscate

#Then build application both .py and .exe
PPrint("Preparing to build application...", "info")
PPrint("Quiz filename? (No extension - Both .py and .exe will get generated)", "module")
name = input("")
#try:
from assets.pybuilder import PiBuilder
PiBuilder().build(name)
#except Exception as e:
#    PPrint(".py Building failed! Erroring out...", "minus")
#    PPrint("Exception: " + str(e), "minus")
#    exit(0)
print("\n")
