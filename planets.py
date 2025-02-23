class Planet:
    def __init__(self, name, ability, multinc, chipinc):
        self.name = name
        self.ability = ability
        self.multinc = multinc
        self.chipinc = chipinc

    def __str__(self):
        return f"{self.name}: {self.ability}"
    
# Base Planets
    
pluto = Planet("Pluto", "Levels up High Card; +1 Mult, +10 Chips", multinc=1, chipinc=10)
mercury = Planet("Mercury", "Levels up Pair; +1 Mult, +15 Chips", multinc=1, chipinc=15)
uranus = Planet("Uranus", "Levels up Two Pair; +1 Mult, +20 Chips", multinc=1, chipinc=20)
venus = Planet("Venus", "Levels up Three of a Kind; +2 Mult, +20 Chips", multinc=2, chipinc=20)
saturn = Planet("Saturn", "Levels up Straight; +3 Mult, +30 Chips", multinc=3, chipinc=30)
jupiter = Planet("Jupiter", "Levels up Flush; +2 Mult, +15 Chips", multinc=2, chipinc=15)
earth = Planet("Earth", "Levels up Full House; +2 Mult, +25 Chips", multinc=2, chipinc=25)
mars = Planet("Mars", "Levels up Four of a Kind; +3 Mult, +30 Chips", multinc=3, chipinc=30)
neptune = Planet("Neptune", "Levels up Straight Flush; +4 Mult, +40 Chips", multinc=4, chipinc=40)

# "Secret" Planets

planetx = Planet("Planet X", "Levels up Five of a Kind; +3 Mult, +35 Chips", multinc=3, chipinc=35)
ceres = Planet("Ceres", "Levels up Flush House; +4 Mult, +40 Chips", multinc=4, chipinc=40)
eris = Planet("Eris", "Levels up Flush Five; +3 Mult, +50 Chips", multinc=3, chipinc=50)