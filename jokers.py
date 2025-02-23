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
        return f"{self.name}: {self.ability}"
    
# base_joker = Joker("Joker", "+4 Mult", )