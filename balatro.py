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
    def __init__(self, asciiart, cardvalue, listvalue, suit):
        self.asciiart = asciiart
        self.cardvalue = cardvalue
        self.listvalue = listvalue
        self.suit = suit

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
    for i in range(8):
        hand.append(deck.pop())
    return hand

def shop():
    print(shop_ascii)
    print("\nImprove your run!")
    print(f"\nMoney: ${player.money}")
    joker1 = choice(jokers)
    new = jokers
    new.remove(joker1)
    joker2 = choice(new)
    planetchoice = choice(planets)
    inshop = [joker1, joker2, planetchoice]
    while True:
        print("\n[N]ext round")
        print("\n[R]eroll ($5)")
        print("\nIn the shop:")
        for i in range(len(inshop)):
            print(f"\n[{i+1}]: {inshop[i]}")
        usrchoice = input("\n").upper()
        optlist = ["N", "R"]
        for i in range(len(inshop)):
            optlist.append(str(i+1))
        if usrchoice not in optlist:
            print("\nValid choice, please.")
            usrchoice = input("\n").upper()
        if usrchoice == "3":
            if player.money >= planetchoice.price:
                inshop.remove(planetchoice)
                planetchoicename = planetchoice.ability.split()
                thishand = planetchoicename[2:(planetchoicename.index("Mult,")-1)]
                thishand = " ".join(thishand)
                thishand = thishand[:-1]
                for i in cardhands:
                    if i.name == thishand:
                        i.lvl += 1
                        print(i)
            else:
                print("\nYou can't buy this!")
        elif usrchoice == "1":
            if player.money >= joker1.price:
                inshop.remove(joker1)
                if "Mult" in joker1.ability:
                    isMult = True
            else:
                print("\nYou can't buy this!")
        elif usrchoice == "2":
            pass
            
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
        thiscard = Card(jacks, "jack", 11, i)
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
        thiscard = Card(queens, "queen", 12, i)
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
        thiscard = Card(kings, "king", 13, i)
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
        thiscard = Card(aces, "ace", 14, i)
        deck.append(thiscard)    

def start_game():
    pass

def pick_hand(hand):
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
    nums.sort(reverse=True)

    if len(set(suits)) == 1 and len(suits) > 1:
        print("Same suit!")
        if len(suits) == 5:
            flagger = []
            for i in range(len(nums)):
                if nums[i] == nums[len(nums)-1]:
                    if nums[i] == nums[i-1]+1:
                        flagger.append(1)
            if len(flagger) > 0:
                print("Straight Flush!")
            else:
                print("Flush!")
    elif len(nums) == 4:
        if len(set(nums)) == 1:
            print("Four of a Kind!")
    elif len(nums) == 5:
        threeof = False
        twoof = False
        for i in nums:
            if nums.count(i) == 3:
                threeof = True
            if nums.count(i) == 2:
                twoof = True
        if threeof and twoof:
            print("Full House")
    elif len(nums) == 5:
        flagger = []
        for i in range(len(nums)):
            if nums[i] == nums[len(nums)-1]:
                if nums[i] == nums[i-1]+1:
                    flagger.append(1)
        if len(flagger) > 0:
            print("Straight!")
    elif len(nums) == 3:
        threeof = False
        for i in nums:
            if nums.count(i) == 3:
                threeof = True
        if threeof:
            print("Three of a Kind")
    elif len(nums) == 4:
        twoof1 = False
        twoof2 = False
        for i in nums:
            if nums.count(i) == 2 and twoof1 == False:
                twoof1 = True
            elif nums.count(i) == 2 and twoof1 == True:
                twoof2 = True
        if twoof1 and twoof2:
            print("Two Pair")
        elif twoof1:
            print("Pair")
        elif twoof2:
            print("Pair")
    elif len(nums) == 2:
        twoof1 = False
        twoof2 = False
        for i in nums:
            if nums.count(i) == 2 and twoof1 == False:
                twoof1 = True
            elif nums.count(i) == 2 and twoof1 == True:
                twoof2 = True
        if twoof1:
            print("Pair")
        elif twoof2:
            print("Pair")
    else:
        print("High Card")

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
    while deckchoice.upper() not in ["R", "B", "BL", "r", "b", "bl", "RED", "BLUE", "BLACK", "YELLOW", "Blue", "Black", "Y", "YELLOW"]:
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

while True:

    make_deck()


    handprint = draw_hand()

    ascii_lines = []

    for i in handprint:
        ascii_line = i.asciiart.split("\n")
        ascii_lines.append(ascii_line)

    for line_set in zip(*ascii_lines):
        print("  ".join(line_set))

    pick_hand(handprint)


# GAME

main_menu()

shop()

run_info()