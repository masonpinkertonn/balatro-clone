# Version: 1.0

# BALATRO clone by Mason P. and Henry C.
# Mr. Smith is him

# Balatro Fetty Wap cover
# YEAHHHHH BABYYY
# UH
# I want you to be mine again Jimbo
# I know my Straight Flush is driving you crazy
# I cannot see myself without you
# we call them jokers girl you know how we do
# I go out of my way to play you
# I go out of my way to score you
# I ain't playing no two pairs I need you
# Baby can you understand Im a young joker living?
# Coming from the deck all a joker know is get it
# I ain't chasing no Two Pair, Jimbo, I'm talkin 'bout that Blueprint
# plus chips in my pockets, all stone cards

# Import local libraries

from balatro_asciis import *
from jokers import *
from planets import *
from balatro_copypasta import *

# Other imports

import sys
from time import *
from random import *
import os
current_mult = 1

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    UNDERLINE = '\033[4m'

# User class
joker_slots_list = []
deck = []
class User:
    def __init__(self, money, hands, discards, jokerslots, roundscore, finalmultinc, finalchipinc, jokers, planetsused, maxhands, maxdiscards):
        self.money = money
        self.hands = hands
        self.discards = discards
        self.jokerslots = jokerslots
        self.roundscore = roundscore
        self.finalmultinc = finalmultinc
        self.finalchipinc = finalchipinc
        self.jokers = jokers
        self.planetsused = planetsused
        self.maxhands = maxhands
        self.maxdiscards = maxdiscards

# Card class

class Card:
    def __init__(self, asciiart, cardvalue, listvalue, suit, multinc = 0, chipinc = 0):
        self.asciiart = asciiart
        self.cardvalue = cardvalue
        self.listvalue = listvalue
        self.suit = suit
        self.multinc = multinc
        self.chipinc = chipinc

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
    
class small_blind:
    def __init__(self, chipval):
        self.chipval = chipval

class big_blind:
    def __init__(self, chipval):
        self.chipval = chipval

class boss_blind:
    def __init__(self, chipval, name):
        self.chipval = chipval
        self.name = name

player = User(0, 4, 3, 5, 0, 0, 0, [], 0, 4, 3)

def playerreset():
    player.hands = player.maxhands
    player.discards = player.maxdiscards
    player.roundscore = 0

stencil_mult2 = player.jokerslots - len(joker_slots_list) 
stencil.multinc = current_mult * stencil_mult2

banner.chipinc = player.discards * 30
usedplanets = 0

if player.discards == 0:
    mystic_summit.multinc = 15
else:
    mystic_summit.multinc = 0

abstract_joker.multinc = len(joker_slots_list) * 3
    
misprint.multinc = randint(1, 23)

blue_joker.chipinc = 2 * len(deck)

constellation_mult2 = int(usedplanets) * 1 
constellation.multinc = current_mult * constellation_mult2

# Main menu
ante = 0
basechips = 0
def uptheante(ante, basechips):
    if ante == 0:
        basechips = 100
    elif ante == 1:
        basechips = 300
    elif ante == 2:
        basechips = 800
    elif ante == 3:
        basechips = 2000
    elif ante == 4:
        basechips = 5000
    elif ante == 5:
        basechips = 11000
    elif ante == 6:
        basechips = 20000
    elif ante == 7:
        basechips = 35000
    elif ante == 8:
        basechips = 50000
    return basechips

straight_flush = Hand("Straight Flush", 100, 8, "same", "5 cards in a row (consecutive ranks) with all cards sharing the same suit")
four_of_a_kind = Hand("Four of a Kind", 60, 7, "any", "4 cards with the same rank. They may be played with 1 other unscored card")
full_house = Hand("Full House", 40, 4, "any", "A Three of a Kind and a Pair")
flush = Hand("Flush", 35, 4, "same", "5 cards that share the same suit")
straight = Hand("Straight", 30, 4, "any", "5 cards in a row (consecutive ranks)")
three_of_a_kind = Hand("Three of a Kind", 30, 3, "any", "3 cards")
two_pair = Hand("Two Pair", 20, 2, "any", "2 pairs of cards with different ranks. May be played with 1 other unscored card.")
pair = Hand("Pair", 10, 2, "any", "2 cards that share the same rank. They may be played with up to 3 other unscored cards")
high_card = Hand("High Card", 5, 1, "any", "If the played hand is not any of the above hands, only the highest rank card scores")

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def wingame():
    jimbosaysifyouwin = randint(1, 10)
    if jimbosaysifyouwin == 1:
        print('\nJimbo says: "You Aced it!"')
    elif jimbosaysifyouwin == 8:
        print('\nJimbo says: "You\'re a Jack of All Trades!"')
    elif jimbosaysifyouwin == 3:
        print('\nJimbo says: "You dealt with that pretty well!"')
    elif jimbosaysifyouwin == 4:
        print('\nJimbo says: "Looks like you weren\'t bluffing!"')
    elif jimbosaysifyouwin == 5:
        print('\nJimbo says: "Too bad these chips are all virtual..."')
    elif jimbosaysifyouwin == 6:
        print('\nJimbo says: "Looks like I\'ve taught you well!"')
    elif jimbosaysifyouwin == 7:
        print('\nJimbo says: "You made some heads up plays!"')
    elif jimbosaysifyouwin == 2:
        print('\nJimbo says: "Good thing I didn\'t bet against you!"')
    elif jimbosaysifyouwin == 9:
        print('\nJimbo says: "You\'re a real card shark!"')
    sys.exit()
def losegame():
    jimbosaysbutyousuck = randint(1, 14)
    if jimbosaysbutyousuck == 1: 
        print('\nJimbo says: "Maybe Go Fish is more our speed..."')
    elif jimbosaysbutyousuck == 11:
        print('\nJimbo says: "You\'re not exactly a card shark..."')
    elif jimbosaysbutyousuck == 2:
        print('\nJimbo says: "We folded like a cheap suit!"')
    elif jimbosaysbutyousuck == 3:
        print('\nJimbo says: "Time for us to shuffle off and try again"')
    elif jimbosaysbutyousuck == 4:
        print('\nJimbo says: "You know what they say, the house always wins!"')
    elif jimbosaysbutyousuck == 5:
        print('\nJimbo says: "Looks like we found out who the real Joker is!"')
    elif jimbosaysbutyousuck == 6:
        print('\nJimbo says: "Oh no, were you bluffing too?"')
    elif jimbosaysbutyousuck == 7:
        print('\nJimbo says: "Looks like the joke\'s on us!"')
    elif jimbosaysbutyousuck == 8:
        print('\nJimbo says: "If I had hands I would have covered my eyes!"')
    elif jimbosaysbutyousuck == 9:
        print('\nJimbo says: "I\'m literally a fool, what\'s your excuse?"')
    elif jimbosaysbutyousuck == 10:
        print('\nJimbo says: "What a flop!"')
    elif jimbosaysbutyousuck == 12:
        print('\nJimbo says: "What did you think you were cooking..."')
    elif jimbosaysbutyousuck == 13:
        balatrocopypasta()
    sys.exit()
    
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


def draw_hand(num):
    shuffle(deck)
    hand = []
    try:
        for i in range(num):
            hand.append(deck.pop())
    except IndexError:
        print("\nNo more cards to draw! You lose!")
        losegame()
    return sorted(hand, key=lambda x: x.listvalue)

def shop():
    print(shop_ascii)
    print("\nImprove your run!")
    joker1 = choice(jokers)
    new = jokers
    new.remove(joker1)
    joker2 = choice(new)
    planetchoice = choice(planets)
    inshop = [joker1, joker2, planetchoice]
    while True:
        print(f"\nMoney: ${player.money}")
        print("\n[N]ext round")
        print("\n[R]eroll ($5)")
        print("\nIn the shop:")
        if len(inshop) == 0:
            print("\nNo items in shop!")
        for i in range(len(inshop)):
            print(f"\n[{i+1}]: {inshop[i]}")
        usrchoice = input("\n").upper()
        optlist = ["N", "R"]
        for i in range(len(inshop)):
            optlist.append(str(i+1))
        while usrchoice not in optlist:
            print("\nValid choice, please.")
            usrchoice = input("\n").upper()
        if usrchoice not in ["N", "R"]:
            usrchoice = inshop[int(usrchoice)-1]
        if isinstance(usrchoice, Planet):
            if player.money >= planetchoice.price:
                player.money -= planetchoice.price
                inshop.remove(planetchoice)
                player.planetsused += 1
                planetchoicename = planetchoice.ability.split()
                thismultinc = int(planetchoicename[planetchoicename.index("Mult,")-1][1])
                thischipinc = int(planetchoicename[planetchoicename.index("Chips")-1][1])
                thishand = planetchoicename[2:(planetchoicename.index("Mult,")-1)]
                thishand = " ".join(thishand)
                thishand = thishand[:-1]
                for i in cardhands:
                    if i.name == thishand:
                        i.lvl += 1
                        i.multval += thismultinc
                        i.chipval += thischipinc
                        print(i)
            else:
                print("\nYou can't buy this!")
        elif isinstance(usrchoice, Joker):
            if player.money >= usrchoice.price and player.jokerslots > 0:
                player.money -= usrchoice.price
                inshop.remove(usrchoice)
                player.jokers.append(usrchoice)
                player.jokerslots -= 1
            else:
                print("\nYou can't buy this!")
            
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
                inshop = [joker1, joker2, planetchoice]
            else:
                print("\nCannot reroll.")

        
    

def make_abandoned_deck(deck):
    for i in ("\u2660", "\u2665", "\u2666", "\u2663"):
        if i == "♥" or i == "♦":
            for y in range(2,10):
                card = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|{y}    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    {y}|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""

                thiscard = Card(card, y, y, i)

                deck.append(thiscard)

            tens = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|{10}   |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|   {10}|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(tens, 10, 10, i)
            deck.append(thiscard)
        
            aces = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|A    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    A|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(aces, 11, 14, i)
            deck.append(thiscard)    
        if i == "♠" or i == "♣":
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

                thiscard = Card(card, y, y, i)

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
            thiscard = Card(tens, 10, 10, i)
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
            thiscard = Card(aces, 11, 14, i)
            deck.append(thiscard)    
    return deck

def make_checkered_deck(deck):
    for i in ("\u2660", "\u2665", "\u2660", "\u2665"):
        if i == "♥":
            for y in range(2,10):
                card = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|{y}    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    {y}|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""

                thiscard = Card(card, y, y, i)

                deck.append(thiscard)

            tens = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|{10}   |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|   {10}|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(tens, 10, 10, i)
            deck.append(thiscard)
            jacks = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|J    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    J|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(jacks, 10, 11, i)
            deck.append(thiscard)
            queens = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|Q    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    Q|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(queens, 10, 12, i)
            deck.append(thiscard)
            kings = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|K    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    K|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(kings, 10, 13, i)
            deck.append(thiscard)
            aces = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|A    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    A|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(aces, 11, 14, i)
            deck.append(thiscard)   
        if i == "♠":
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

                thiscard = Card(card, y, y, i)

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
            thiscard = Card(tens, 10, 10, i)
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
            thiscard = Card(jacks, 10, 11, i)
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
            thiscard = Card(queens, 10, 12, i)
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
            thiscard = Card(kings, 10, 13, i)
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
            thiscard = Card(aces, 11, 14, i)
            deck.append(thiscard)   
    return deck

def make_deck(deck):
    for i in ("\u2660", "\u2665", "\u2666", "\u2663"):
        if i == "♥" or i == "♦":
            for y in range(2,10):
                card = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|{y}    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    {y}|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""

                thiscard = Card(card, y, y, i)

                deck.append(thiscard)

            tens = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|{10}   |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|   {10}|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(tens, 10, 10, i)
            deck.append(thiscard)
            jacks = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|J    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    J|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(jacks, 10, 11, i)
            deck.append(thiscard)
            queens = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|Q    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    Q|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(queens, 10, 12, i)
            deck.append(thiscard)
            kings = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|K    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    K|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(kings, 10, 13, i)
            deck.append(thiscard)
            aces = f"""{bcolors.RED} {bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
{bcolors.RED}|A    |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|  {i}  |{bcolors.ENDC}
{bcolors.RED}|     |{bcolors.ENDC}
{bcolors.RED}|    A|{bcolors.ENDC}
{bcolors.RED} ----- {bcolors.ENDC}
                {bcolors.RED}{bcolors.ENDC}"""
            thiscard = Card(aces, 11, 14, i)
            deck.append(thiscard)   
        if i == "♠" or i == "♣":
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

                thiscard = Card(card, y, y, i)

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
            thiscard = Card(tens, 10, 10, i)
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
            thiscard = Card(jacks, 10, 11, i)
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
            thiscard = Card(queens, 10, 12, i)
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
            thiscard = Card(kings, 10, 13, i)
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
            thiscard = Card(aces, 11, 14, i)
            deck.append(thiscard)   
    return deck
def start_game():
    pass

def pick_hand(hand, cardhands):
    print("\nPlease select the indices of the cards you wish to select, separated by commas.")
    indiceschoice = input("\n")
    indiceschoice = indiceschoice.split(", ")
    while (len(indiceschoice) != len(set(indiceschoice))) or (len(indiceschoice) > 5):
        print("\nPlease input a valid response.")
        sleep(1)
        print("\nPlease select the indices of the cards you wish to play, separated by commas.")
        indiceschoice = input("\n")
        indiceschoice = indiceschoice.split(", ")
    cards = []
    for i in indiceschoice:
        cards.append(hand[int(i)-1])
    ascii_lines = []
    for i in cards:
        ascii_line = i.asciiart.split("\n")
        ascii_lines.append(ascii_line)

    for line_set in zip(*ascii_lines):
        print("  ".join(line_set))

    suits = []
    nums = []

    for i in cards:
        suits.append(i.suit)
        if isinstance(i.listvalue, int):
            nums.append(i.listvalue)
        else:
            nums.append(i.listvalue)
    unsortednums = nums.copy()
    nums.sort(reverse=True)

    those = []
    these = []

    if len(set(suits)) == 1 and len(suits) > 1:
        if len(suits) == 5:
            flagger = []
            for i in range(len(nums)):
                if nums[i] != nums[len(nums)-1]:
                    if nums[i] == nums[i+1]+1:
                        flagger.append("1")
            if len(flagger) == 4:
                print("Straight Flush!")
                return (cards, cardhands[0], cards)
            else:
                print("Flush!")
                return (cards, cardhands[3], cards)

    for i in range(1, 15):
        scoring = []
        ts = nums.count(i)
        if ts == 4:
            print("Four of a Kind!")
            for index, number in enumerate(unsortednums):
                if number == i:
                    scoring.append(cards[index])
            return (scoring, cardhands[1], cards)
        elif ts == 3:
            these.append(ts)
        elif ts == 2:
            those.append(ts)
    seen = set()
    dupes = []

    for x in unsortednums:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)
    if len(those) == 1 and len(these) == 1:
        print("Full House")
        scoring = []
        for i, z in enumerate(unsortednums):
            if z in dupes:
                scoring.append(cards[i])
        return (scoring, cardhands[2], cards)
    elif len(those) == 2:
        print("Two Pair")
        scoring = []
        for i, z in enumerate(unsortednums):
            if z in dupes:
                scoring.append(cards[i])
        return (scoring, cardhands[6], cards)
    elif len(these) == 1:
        print("Three of a Kind")
        scoring = []
        for i, z in enumerate(unsortednums):
            if z in dupes:
                scoring.append(cards[i])
        return (scoring, cardhands[5], cards)
    elif len(those) == 1:
        print("Pair")
        scoring = []
        for i, z in enumerate(unsortednums):
            if z in dupes:
                scoring.append(cards[i])
        return (scoring, cardhands[7], cards)
    if len(nums) == 5:
        flagger = []
        for i in range(len(nums)):
            if nums[i] != nums[-1]:
                if nums[i] == nums[i+1]+1:
                    flagger.append('1')
        if len(flagger) == 4:
            print("Straight!")
            return (cards, cardhands[4], cards)        
    print("High Card!")
    thisstuff = max(nums)
    for i in cards:
        if i.listvalue == thisstuff:
            mylist = []
            mylist.append(i)
            return(mylist, cardhands[8], cards)

def main_menu(ante, basechips, cardhands):
    while True:
        print(balatro_title_text)
        print("[P]lay        [Q]uit        [C]ollection")
        usr_choice = input("\n").upper()
        while usr_choice not in ("P", "Q", "C"):
            print("\nPlease enter a valid choice.")
            usr_choice = input("\n").upper()
        if usr_choice == "P":
            rungame(ante, basechips, cardhands)
        elif usr_choice == "Q":
            print("\nShutting down...\n")
            sleep(2)
            sys.exit()
        elif usr_choice == "C":
            print(joker_ascii)
            sleep(2)
            for i in jokers:
                print("\n")
                print(i)
            sleep(2)
            print(planet_ascii)
            sleep(2)
            for i in planets:
                print("\n")
                print(i)
            sleep(2)

def smallpayout():
    interest = (player.money // 5)
    if interest > 5:
        interest = 5
    player.money += interest
    player.money += player.hands
    player.money += 3
def bigpayout():
    interest = (player.money // 5)
    if interest > 5:
        interest = 5
    player.money += interest
    player.money += player.hands
    player.money += 4
def bosspayout():
    interest = (player.money // 5)
    if interest > 5:
        interest = 5
    player.money += interest
    player.money += player.hands
    player.money += 5
def finisherpayout():
    interest = (player.money // 5)
    if interest > 5:
        interest = 5
    player.money += interest
    player.money += player.hands
    player.money += 8

def choose_deck():
    hasdeckbeenchosen = True
    while hasdeckbeenchosen:
        deckchoice = input("\nChoose a deck: [R]ed, [B]lue, [Bl]ack, [A]bandoned, [C]heckered, [Y]ellow, or type [I]nfo: ").upper()
        while deckchoice.upper() not in ["R", "B", "BL", "r", "b", "bl", "RED", "BLUE", "BLACK", "YELLOW", "Blue", "Black", "Y", "YELLOW", "a", "A", "ABANDONED", "C", "CHECKERED", "I", "INFO",]:
            print("\nPlease enter a valid choice.")
            deckchoice = input("\nChoose a deck: [R]ed, [B]lue, [Bl]ack, [A]bandoned, or [Y]ellow: ").upper()
        if deckchoice.upper() in ["R", "RED"]:
            print("\nYou chose the Red deck.")
            make_deck(deck)
            player.discards += 1
            hasdeckbeenchosen = False
        if deckchoice.upper() in ["B", "BLUE"]:
            print("\nYou chose the Blue deck.")
            make_deck(deck)
            player.hands += 1
            hasdeckbeenchosen = False
        if deckchoice.upper() in ["BL", "BLACK"]:
            print("\nYou chose the Black deck.")
            make_deck(deck)
            player.jokerslots += 1
            hasdeckbeenchosen = False
        if deckchoice.upper() in ["A", "ABANDONED"]:
            print("\nYou chose the Abandoned deck.")
            make_abandoned_deck(deck)
            hasdeckbeenchosen = False
        if deckchoice.upper() in ["Y", "YELLOW"]:
            print("\nYou chose the Yellow deck.")
            make_deck(deck)
            player.money += 10
            hasdeckbeenchosen = False
        if deckchoice.upper() in ["C", "CHECKERED"]:
            print("\nYou chose the Checkered deck.")
            make_checkered_deck(deck)
            
        
            hasdeckbeenchosen = False
        if deckchoice.upper() in ["I", "INFO"]:
            whichdeckinfo = input("\nWhich deck would you like to know more about? [R]ed, [B]lue, [Bl]ack, [A]bandoned, [C]heckered, [Y]ellow: ").upper()
            while whichdeckinfo not in ["R", "RED", "B", "BLUE", "BL", "BLACK", "A", "ABANDONED", "C", "CHECKERED", "Y", "YELLOW", ]:
                print("\nPlease enter a valid choice.")
                whichdeckinfo = input("\nWhich deck would you like to know more about? [R]ed, [B]lue, [Bl]ack, [A]bandoned, [C]heckered, [Y]ellow: ").upper()
            if whichdeckinfo in ["R", "RED"]:
                print("\nRed Deck: The Red Deck gives you +1 Discard")
            if whichdeckinfo in ["B", "BLUE"]:
                print("\nBlue Deck: The Blue Deck gives you +1 Hand")
            if whichdeckinfo in ["BL", "BLACK"]:
                print("\nBlack Deck: The Black Deck gives you +1 Joker Slot")
            if whichdeckinfo in ["A", "ABANDONED"]:
                print("\nAbandoned Deck: The Abandoned Deck has no Face Cards")
            if whichdeckinfo in ["C", "CHECKERED"]:
                print("\nCheckered Deck: The Checkered Deck only has Hearts and Spades")
            if whichdeckinfo in ["Y", "YELLOW"]:
                print("\nYellow Deck: The Yellow Deck gives you $10 at the beginning of the run")
    return deckchoice.upper()

def scorejokers(tssshand, totalmult, totalchips):
    if (len(player.jokers)) != 0:
        print("\nHow do you want to arrange your jokers? Current order:")
        for index, value in enumerate(player.jokers):
            print("\n[" + str(index+1) + "]: " + str(value))
        rearrange = input("\n")
        tss = rearrange.split(", ")
        for i in range(len(tss)):
            tss[i] = int(tss[i]) - 1
        for i in tss:
            okok = player.jokers[i].name
            okokok = player.jokers[i].ability
            if "Mult" in okokok:
                match = []
                if okok == "Jimbo":
                    totalmult += 4
                    print("\n+4 Total Mult")
                if "Played cards with" in okokok:
                    x = okokok.split(" ")
                    inc = x[6]
                    inc = int(inc[1])
                    important = x[3].lower()
                    if important == "club":
                        important = "\u2663"
                    elif important == "spade":
                        important = "\u2660"
                    elif important == "heart":
                        important = "\u2665"
                    elif important == "diamond":
                        important = "\u2666"
                    for index, value in enumerate(tssshand[0]):
                        if value.suit == important:
                            totalmult += inc
                            print(f"\n+{inc} mult for {value.listvalue} of {value.suit}")
                if "if played hand contains a" in okokok:
                    x = okokok.split(" ")
                    inc = x[0]
                    inc = int(inc[1:])
                    important = x[7:]
                    tss = ' '.join(important)
                    for i in cardhands:
                        if tssshand[1].name == i.name:
                            totalmult += inc
                            print(f"\n+{inc} mult for {i.name} hand")
                            break
                if okok == "Half Joker":
                    if len(tssshand[2]) <= 3:
                        totalmult += 20
                        print("\n+20 Mult from Half Joker")
                if okok == "Misprint":
                    thissmult = randint(0, 24)
                    totalmult += thissmult
                    print(f"\n+{thissmult} from Misprint")
                if okok == "Stencil":
                    totalmult *= player.jokerslots
                    print(f"\n*{player.jokerslots} Mult from Stencil")
                if okok == "Mystic Summit":
                    if player.discards <= 0:
                        totalmult += 15
                        print(f"\n+15 Mult from Mystic Summit")
                if okok == "Abstract Joker":
                    totalmult += (3*(5-player.jokerslots))
                    print(f"\n+{(3*(5-player.jokerslots))} Mult from Abstract Joker")
                if okok == "Constellation":
                    totalmult *= (player.planetsused)
                    print(f"\n*{player.planetsused} Mult from Constellation")
            if "Chips" in okokok:
                if "if played hand contains a" in okokok:
                    x = okokok.split(" ")
                    inc = x[0]
                    inc = int(inc[1:])
                    important = x[7:]
                    tss = ' '.join(important)
                    for i in cardhands:
                        if tssshand[1].name == i.name:
                            totalchips += inc
                            print(f"\n+{inc} Chips for {i.name} hand")
                            break
                if okok == "Banner":
                    totalchips += (player.discards * 30)
                    print(f"\n+{player.discards * 30} Chips from Banner")
                if okok == "Blue Joker":
                    totalchips += (2*len(deck))
                    print(f"\n+{(2*len(deck))} Chips from Blue Joker")
    return (totalmult, totalchips)

def blindfunction(blind, ante, basechips, cardhands):
    handprint = draw_hand(8)
    while (player.roundscore < blind.chipval):
        if player.hands <= 0:
            print("\nYou Lose!")
            sys.exit()
        displayhand(handprint)
        tssshand = pick_hand(handprint, cardhands)
        print("\n[P]lay hand        [D]iscard hand        [R]un info") # We need to place restraints (only 5 cards can be discarded)
        whatdoyoudo = input("\n").upper()
        if whatdoyoudo == "P":
            totalmult = 0
            totalchips = 0
            ## PLAY HAND
            for i in tssshand[0]:
                totalchips += i.cardvalue 
                totalmult += i.multinc
            totalmult += tssshand[1].multval
            totalchips += tssshand[1].chipval
            mason = scorejokers(tssshand, totalmult, totalchips)
            new = (mason[1]) * (mason[0])
            if new >= blind.chipval:
                print(f"\n\U0001F525 {mason[1]} x {mason[0]} \U0001F525")
            else:
                print(f"\n{mason[1]} x {mason[0]}")
            print("\n"+str(new))
            player.roundscore += new
            if player.roundscore < blind.chipval:
                y = list(set(handprint) - set(tssshand[2]))
                y = sorted(y, key=lambda x: x.listvalue)
                newhp = draw_hand(len(tssshand[2]))
                newlist = newhp + y
                handprint = sorted(newlist, key=lambda x: x.listvalue)
            player.hands -= 1
            print(f"\nYou have {player.hands} hands left")
            if player.roundscore < blind.chipval:
                print(f"\nYou need {basechips - player.roundscore} more chips")
            else:
                print("\nYou need 0 more chips")
        elif whatdoyoudo == "D":
            ## DISCARD HAND
            if player.discards > 0:
                player.discards -= 1
                y = list(set(handprint) - set(tssshand[2]))
                y = sorted(y, key=lambda x: x.listvalue)
                newhp = draw_hand(len(tssshand[2]))
                newlist = newhp + y
                handprint = sorted(newlist, key=lambda x: x.listvalue)
                print(f"\nDiscards: {player.discards}")
            else:
                print("\nNo discards left!")
        elif whatdoyoudo in ["R", "RUN INFO", "RUN", "RUNINFO", "INFO", "I"]:
            run_info()
        else: 
            print("Please enter a valid choice.")
        if player.roundscore > blind.chipval:
            print("\nYou beat the boss blind!")
def bossblindfunction(ante, basechips, cardhands):
    bossbasechips = (basechips * 2)
    needlebasechips = (basechips * 1.75)
    selected_bosses = set()
    available_bosses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if len(selected_bosses) == len(available_bosses):
        print("All bosses have already been selected.")
        return None
    while True:
        whichboss = choice(available_bosses)
        if whichboss not in selected_bosses:
            selected_bosses.add(whichboss)  
            break
    if whichboss == 1:
        print("The Wall: A very large blind.")
        wallbasechips = (basechips * 4)
        bossblind = boss_blind(wallbasechips, "The Wall")
    if whichboss == 2:
        print("The Water: No discards.")
        bossblind = boss_blind(bossbasechips, "The Water")
        player.discards = 0
    if whichboss == 3:
        print("The Needle: Only play 1 hand.")
        bossblind = boss_blind(needlebasechips, "The Needle")
        player.hands = 1
    if whichboss == 4:
        print("The Box: A very, very large blind, All discards become hands.")
        boxchips = (basechips * 6)
        player.hands += player.discards
        player.discards = 0
        bossblind = boss_blind(boxchips, "The Box")
    if whichboss == 5:
        print("The Imposter: Just a big blind who got a surprise promotion.")
        imposterbasechips = (basechips * 1.5)
        imposterbasechips = int(imposterbasechips)
        bossblind = boss_blind(imposterbasechips, "The Imposter")
    if whichboss == 6:
        print("The Stone: +1x Base score for every $10 held ")
        stonechipsmultiplier = (player.money // 10)
        stonechips = (basechips * stonechipsmultiplier)
        bossblind = boss_blind(stonechips, "The Stone")
    if whichboss == 7:
        print("The Sand: +1x Base score for every Joker")
        sandchipsmultiplier = len(player.jokers)
        sandchips = (basechips * sandchipsmultiplier)
        bossblind = boss_blind(sandchips, "The Sand")
    if whichboss == 8:
        print("The Glass: +1x Base score for every Discard")
        glasschipsmultiplier = player.discards
        glasschips = (basechips * glasschipsmultiplier)
        bossblind = boss_blind(glasschips, "The Glass")
    if whichboss == 9:
        print("The Mirror: +1x Base score for every Hand")
        mirrorchipsmultiplier = player.hands
        mirrorchips = (basechips * mirrorchipsmultiplier)
        bossblind = boss_blind(mirrorchips, "The Mirror")
    return bossblind

        


def finisherblindfunction(ante, basechips, cardhands):
    whichfinisher = randint(1,5)
    if whichfinisher == 1:
        print("Violet Vessel: A very, very, large blind.")
        violetvesselchips = (basechips * 6)
        finisherblind = boss_blind(violetvesselchips, "Violet Vessel")
    if whichfinisher == 2:
        print("Silver Sword: A large blind, only play one hand.")
        player.hands == 1
        silverswordchips = basechips * 3
        finisherblind = boss_blind(silverswordchips, "Silver Sword")
    if whichfinisher == 3:
        print("Golden Goblet: A large blind, no discards.")
        player.discards = 0
        goldengobletchips = basechips * 3
        finisherblind = boss_blind(goldengobletchips, "Golden Goblet")
    if whichfinisher == 4:
        print("Bronze Bow: A large blind, all discards become hands, all hands become discards.")
        bronzebowhands = player.discards
        bronzebowdiscards = player.hands
        player.hands = bronzebowhands
        player.discards = bronzebowdiscards
        bronzebowchips = basechips * 3
        finisherblind = boss_blind(bronzebowchips, "Bronze Bow")
    return finisherblind

    

def rungame(ante, basechips, cardhands):
    z = choose_deck()
    round = 0
    while player.hands > 0:
        ante += 1
        x = uptheante(ante, basechips)
        restore = x
        print(f"\nSMALL BLIND: {x} chips to defeat")
        smallblind = small_blind(x)
        blindfunction(smallblind, ante, x, cardhands)
        smallpayout()
        round += 1
        playerreset()
        shop()
        deck = []
        if z in ("A", "ABANDONED"):
            deck = make_abandoned_deck(deck)
        elif z in ("C", "CHECKERED"):
            deck = make_checkered_deck(deck)
        else:
            deck = make_deck(deck)
        print(len(deck))
        x *= 1.5
        x = int(x)
        print(f"\nBIG BLIND: {x} chips to defeat")
        bigblind = big_blind(x)
        blindfunction(bigblind, ante, x, cardhands)
        bigpayout()
        round += 1
        playerreset()
        shop()
        deck = []
        if z in ("A", "ABANDONED"):
            deck = make_abandoned_deck(deck)
        elif z in ("C", "CHECKERED"):
            deck = make_checkered_deck(deck)
        else:
            deck = make_deck(deck)
        print(len(deck))
        restore *= 2
        tsssss = bossblindfunction(ante, restore, cardhands)
        blindfunction(tsssss, ante, restore, cardhands)
        bosspayout()
        round += 1
        playerreset()
        shop()
        deck = []
        if z in ("A", "ABANDONED"):
            deck = make_abandoned_deck(deck)
        elif z in ("C", "CHECKERED"):
            deck = make_checkered_deck(deck)
        else:
            deck = make_deck(deck)
        if ante == 8:
            mystuff = finisherblindfunction(ante, restore, cardhands)
            blindfunction(mystuff, ante, restore, cardhands)
            wingame()
            shop()
    losegame()
        

def displayhand(handprint):
    ascii_lines = []

    for i in handprint:
        ascii_line = i.asciiart.split("\n")
        ascii_lines.append(ascii_line)

    for line_set in zip(*ascii_lines):
        print("  ".join(line_set))

    for i in range(len(handprint)):
        print("   " + str(i+1)+"    ", end=" ")
    print()

# GAME

main_menu(ante, basechips, cardhands)

shop()

run_info()

clear_terminal()
