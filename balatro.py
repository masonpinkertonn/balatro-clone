# BALATRO clone by Mason P. and Henry C.

# Import local libraries

from balatro_asciis import *
from jokers import *
from planets import *

# Other imports

import sys
from time import *
from random import *
current_mult = 1
# User class
joker_slots_list = []
deck = []
class User:
    def __init__(self, money, hands, discards, jokerslots, roundscore):
        self.money = money
        self.hands = hands
        self.discards = discards
        self.jokerslots = jokerslots
        self.roundscore = roundscore

# Card class

class Card:
    def __init__(self, asciiart, value):
        self.asciiart = asciiart
        self.value = value

    def __str__(self):
        return self.asciiart
    
# Hand class

class Hand:
    def __init__(self, name, chipval, multval, suit, cards, lvl=1):
        self.name = name
        self.chipval = chipval
        self.multval = multval
        self.suit = suit
        self.cards = cards
        self.lvl = lvl

    def __str__(self):
        return f"\nLevel {self.lvl} {self.name}: {self.cards}"

player = User(0, 4, 3, 5, 0)

stencil_mult2 = player.jokerslots - len(joker_slots_list) 
stencil.multinc = current_mult * stencil_mult2

banner.chipinc = player.discards * 30


if player.discards == 0:
    mystic_summit.multinc = 15
else:
    mystic_summit.multinc = 0

abstract_joker.multinc = len(joker_slots_list) * 3
    
misprint.multinc = randint(1, 23)

blue_joker.chipinc = 2 * len(deck)
# Main menu

straight_flush = Hand("Straight Flush", 100, 8, "same", "5 cards in a row (consecutive ranks) with all cards sharing the same suit")
four_of_a_kind = Hand("Four of a Kind", 60, 7, "any", "4 cards with the same rank. They may be played with 1 other unscored card")
full_house = Hand("Full House", 40, 4, "any", "A Three of a Kind and a Pair")
flush = Hand("Flush", 35, 4, "same", "5 cards that share the same suit")
straight = Hand("Straight", 30, 4, "any", "5 cards in a row (consecutive ranks)")
three_of_a_kind = Hand("Three of a Kind", 30, 3, "any", "3 cards")
two_pair = Hand("Two Pair", 20, 2, "any", "2 pairs of cards with different ranks. May be played with 1 other unscored card.")
pair = Hand("Pair", 10, 2, "any", "2 cards that share the same rank. They may be played with up to 3 other unscored cards")
high_card = Hand("High Card", 5, 1, "any", "If the played hand is not any of the above hands, only the highest rank card scores")


def run_info():
    print("\nPOKER HANDS")
    print(straight_flush)
    print(four_of_a_kind)
    print(full_house)
    print(flush)
    print(straight)
    print(three_of_a_kind)
    print(two_pair)
    print(pair)
    print(high_card)

cardhands = [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, pair, high_card]


def draw_hand():
    shuffle(deck)
    hand = []
    for i in range(5):
        hand.append(deck.pop())
    return hand[0]

def shop():
    print(shop_ascii)
    print("\nImprove your run!")
    print(f"\nMoney: ${player.money}")
    print("\n[N]ext round")
    print("\n[R]eroll ($5)")
    print("\nIn the shop:")
    joker1 = choice(jokers)
    new = jokers
    new.remove(joker1)
    joker2 = choice(new)
    planetchoice = choice(planets)
    while True:
        print(f"\n[1]: {joker1}")
        print(f"\n[2]: {joker2}")
        print(f"\n[3]: {planetchoice}")
        usrchoice = input("\n").upper()
        if usrchoice not in ("1", "2", "3", "N", "R"):
            print("\nValid choice, please.")
            usrchoice = input("\n").upper()
        if usrchoice == "3":
            planetchoicename = planetchoice.ability.split()
            thishand = planetchoicename[2:(planetchoicename.index("Mult,")-1)]
            thishand = " ".join(thishand)
            thishand = thishand[:-1]
            for i in cardhands:
                if i.name == thishand:
                    i.lvl += 1
                    print(i)
        elif usrchoice == "N":
            break
        elif usrchoice == "R":
            if player.money >= 5:
                player.money -= 5
                joker1 = choice(jokers)
                new = jokers
                new.remove(joker1)
                joker2 = choice(new)
                planetchoice = choice(planets)
            else:
                print("\nCannot reroll.")

        
    

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
        jacks = f""" 
 ----- 
|J    |
|     |
|  {i}  |
|     |
|    J|
 -----
        """
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
    print("[P]lay        [Q]uit        [C]ollection")
    usr_choice = input("\n").upper()
    while usr_choice not in ("P", "Q", "C"):
        print("\nPlease enter a valid choice.")
        usr_choice = input("\n").upper()
    if usr_choice == "P":
        start_game()
    elif usr_choice == "Q":
        print("\nShutting down...")
        sleep(2)
        sys.exit()
    elif usr_choice == "C":
        pass
def choose_deck():
    deckchoice = input("\nChoose a deck: [R]ed, [B]lue, [Bl]ack, or [Y]ellow: ").upper()
    while deckchoice not in ["R", "B", "Bl", "r", "b", "bl", "red", "blue", "black", "Red", "Blue", "Black", "Y", "YELLOW"]:
        print("\nPlease enter a valid choice.")
        deckchoice = input("\nChoose a deck: [R]ed, [B]lue, [Bl]ack, or [Y]ellow: ").upper()
    if deckchoice.upper() in ["R", "RED"]:
            player.discards += 1
    if deckchoice.upper() in ["B", "BLUE"]:
            player.hands += 1
    if deckchoice.upper() in ["BL", "BLACK"]:
        player.jokerslots += 1
        player.hands -= 1
    if deckchoice.upper() in ["Y", "YELLOW"]:
        player.money += 10

choose_deck()
class small_blind:
    def __init__(self, chipval):
        self.chipval = chipval

class big_blind:
    def __init__(self, chipval):
        self.chipval = chipval

class boss_blind:
    def __init__(self, chipval, name, modifier):
        self.chipval = chipval
        self.name = name
        self.modifier = modifier


make_deck()


handprint = draw_hand()
print(handprint)

# GAME

main_menu()

shop()

run_info()