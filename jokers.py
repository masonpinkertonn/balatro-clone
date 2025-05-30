from random import *

class Joker:
    def __init__(self, name, ability, multinc, chipinc, suit, hand, price, rarity):
        self.name = name
        self.ability = ability
        self.multinc = multinc
        self.chipinc = chipinc
        self.suit = suit
        self.hand = hand
        self.price = price
        self.rarity = rarity
    
    def __str__(self):
        return f"${self.price} | {self.name}: {self.ability}"

misprint_mult = 0
stencil_mult = 0
banner_chips = 0
mystic_mult = 0
abstract_mult = 0
blue_joker_chips = 0
constellation_mult = 0

base_joker = Joker("Jimbo", "+4 Mult", 4, 0, "all", "all", 2, "common")
greedy_joker = Joker("Greedy Joker", "Played cards with Diamond suit give +3 Mult when scored", 3, 0, "diamond", "all", 5, "common")
lusty_joker = Joker("Lusty Joker", "Played cards with Heart suit give +3 Mult when scored", 3, 0, "heart", "all", 5, "common")
wrathful_joker = Joker("Wrathful Joker", "Played cards with Spade suit give +3 Mult when scored", 3, 0, "spade", "all", 5, "common")
gluttonous_joker = Joker("Gluttonous Joker", "Played cards with Club suit give +3 Mult when scored", 3, 0, "club", "all", 5, "common")
jolly_joker = Joker("Jolly Joker", "+8 Mult if played hand contains a Pair", 8, 0, "all", "pair", 3, "common")
zany_joker = Joker("Zany Joker", "+12 Mult if played hand contains a Three of a Kind", 12, 0, "all", "three of a kind", 4, "common")
mad_joker = Joker("Mad Joker", "+10 Mult if played hand contains a Two Pair", 10, 0, "all", "two pair", 4, "common")
crazy_joker = Joker("Crazy Joker", "+12 Mult if played hand contains a Straight", 12, 0, "all", "straight", 4, "common")
droll_joker = Joker("Droll Joker", "+10 Mult if played hand contains a Flush", 10, 0, "all", "flush", 4, "common")
sly_joker = Joker("Sly Joker", "+50 Chips if played hand contains a Pair", 0, 50, "all", "pair", 3, "common")
wily_joker = Joker("Wily Joker", "+100 Chips if played hand contains a Three of a Kind", 0, 100, "all", "three of a kind", 4, "common")
clever_joker = Joker("Clever Joker", "+80 Chips if played hand contains a Two Pair", 0, 80, "all", "two pair", 4, "common")
devious_joker = Joker("Devious Joker", "+100 Chips if played hand contains a Straight", 0, 100, "all", "straight", 4, "common")
crafty_joker = Joker("Crafty Joker", "+80 Chips if played hand contains a Flush", 0, 80, "all", "flush", 4, "common")
half_joker = Joker("Half Joker", "+20 Mult if played hand contains 3 or fewer cards", 20, 0, "all", "3 or less", 5, "common")
misprint = Joker("Misprint", "+? Mult", misprint_mult, 0, "all", "tens", 5, "common")
stencil = Joker("Stencil", "Gains x1 Mult for each empty Joker Slot", stencil_mult, 0, "all", "all", 5, "common")
banner = Joker("Banner", "Gains +30 Chips for each remaining discard", 0, banner_chips, "all", "all", 5, "common")
mystic_summit = Joker("Mystic Summit", "Gains +15 Mult if 0 discards remaining", mystic_mult, 0, "all", "all", 6, "rare")
abstract_joker = Joker("Abstract Joker", "Gains +3 Mult for each joker card", abstract_mult, 0, "all", "all", 6, "rare")
blue_joker = Joker("Blue Joker", "+2 Chips for each card remaining in deck", 0, blue_joker_chips, "all", "pair", 3, "common")
constellation = Joker("Constellation", "Gains +0.2 Mult for each Planet Card used", constellation_mult, 0, "all", "all", 6, "rare")


jokers = [base_joker, greedy_joker, lusty_joker, wrathful_joker, gluttonous_joker, jolly_joker, zany_joker, mad_joker, crazy_joker, droll_joker, sly_joker, wily_joker, clever_joker, devious_joker, crafty_joker, half_joker, misprint, stencil, banner, mystic_summit, abstract_joker, blue_joker, constellation]