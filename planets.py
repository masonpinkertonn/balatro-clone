class Planet:
    def __init__(self, name, ability, multinc, chipinc, price=3):
        self.name = name
        self.ability = ability
        self.multinc = multinc
        self.chipinc = chipinc
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.ability}"
    
# Base Planets
    
pluto = Planet("Pluto", "Levels up High Card; +1 Mult, +10 Chips", 1, 10)
mercury = Planet("Mercury", "Levels up Pair; +1 Mult, +15 Chips", 1, 15)
uranus = Planet("Uranus", "Levels up Two Pair; +1 Mult, +20 Chips", 1, 20)
venus = Planet("Venus", "Levels up Three of a Kind; +2 Mult, +20 Chips", 2, 20)
saturn = Planet("Saturn", "Levels up Straight; +3 Mult, +30 Chips", 3, 30)
jupiter = Planet("Jupiter", "Levels up Flush; +2 Mult, +15 Chips", 2, 15)
earth = Planet("Earth", "Levels up Full House; +2 Mult, +25 Chips", 2, 25)
mars = Planet("Mars", "Levels up Four of a Kind; +3 Mult, +30 Chips", 3, 30)
neptune = Planet("Neptune", "Levels up Straight Flush; +4 Mult, +40 Chips", 4, 40)

planets = [pluto, mercury, uranus, venus, saturn, jupiter, earth, mars, neptune]