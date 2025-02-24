# BALATRO clone by Mason P. and Henry C.

# Import local libraries

from balatro_asciis import *
from jokers import *
from planets import *

# Other imports

import sys
from time import *
from random import *

# Card class

class Card:
    def __init__(self, asciiart, value):
        self.asciiart = asciiart
        self.value = value

    def __str__(self):
        return self.asciiart

# Main menu

deck = []

def make_deck():
    for i in ("\u2660", "\u2665", "\u2666", "\u2663"):
        for y in range(2,10):
            card = f""" 
 ----- 
|{y}    |
|     |
|  {i}  |
|     |
|    {y}|
 -----
            """

            thiscard = Card(card, y)

            deck.append(thiscard)

        tens = f""" 
 ----- 
|{10}   |
|     |
|  {i}  |
|     |
|   {10}|
 -----
        """
        thiscard = Card(tens, 10)
        deck.append(thiscard)
        jacks = print(f""" 
 ----- 
|J    |
|     |
|  {i}  |
|     |
|    J|
 -----
        """)
        thiscard = Card(jacks, "jack")
        deck.append(thiscard)
        queens = f""" 
 ----- 
|Q    |
|     |
|  {i}  |
|     |
|    Q|
 -----
        """
        thiscard = Card(queens, "queen")
        deck.append(thiscard)
        kings = f""" 
 ----- 
|K    |
|     |
|  {i}  |
|     |
|    K|
 -----
        """
        thiscard = Card(kings, "king")
        deck.append(thiscard)
        aces = f""" 
 ----- 
|A    |
|     |
|  {i}  |
|     |
|    A|
 -----
        """
        thiscard = Card(aces, "ace")
        deck.append(thiscard)

    

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

"""

def draw_hand():
    shuffle(deck)
    hand = []
    for i in range(5):
        hand.append(deck.pop())
    return hand

handprint = draw_hand()
print(handprint)
# GAME

main_menu()

"""

make_deck()