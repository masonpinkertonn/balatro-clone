# BALATRO clone by Mason P. and Henry C.

# Import local libraries

from balatro_asciis import *
from jokers import *
from planets import *

x = """
 ----- 
|3    |
|     |
|  \u2660  |
|     |
|    3|
 -----
"""

print(x)

# Other imports

import sys
from time import *

# Main menu

def make_deck():
    for i in ("\u2660", "\u2665", "\u2666", "\u2663"):
        for y in range(2,10):
            card = f""" 
 ----- 
|{y}    |
|     |
|  \u2660  |
|     |
|    {y}|
 -----
            """
            print(card)

    

def start_game():
    pass

def main_menu():
    print(balatro_title_text)
    print("[P]lay        [O]ptions        [Q]uit        [C]ollection")
    usr_choice = input("\n").upper()
    while usr_choice not in ("P", "O", "Q", "C"):
        print("\nPlease enter a valid choice.")
        usr_choice = input("\n").upper()
    if usr_choice == "P":
        start_game()
    elif usr_choice == "O":
        pass
    elif usr_choice == "Q":
        print("\nShutting down...")
        sleep(2)
        sys.exit()
    elif usr_choice == "C":
        pass

# GAME

make_deck()

main_menu()