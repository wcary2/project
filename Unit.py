import random
class Unit:
    def __init__(self, armor, attack, defense, dsize, name):
        self.name = name
        self.armor = armor
        self.attack = attack
        self.dSize = dsize
        self.defense = defense

    def roll(range):
        return random.randrange(1, range)

    def rattack(self):
        return self.roll(self.attack)

    def rdefend(self):
        return self.roll(self.defense)

    def modHealth(self, change):
        self.armor += change

class Infantry(Unit):
    def _init(self):
        Unit.__init__(self, 2, 1, 2, 4, "Infantry")


class Artillery(Unit):
    def _init(self):
        Unit.__init__(self, 2, 2, 2, 4, "Artillery")

class Tank(Unit):
    def __init__(self):
        Unit.__init__(self, 3, 3, 3, 4, "Tank")


class Fighter(Unit):
    def __init__(self):
        Unit.__init__(self, 3, 3, 4, 6, "Fighter")


class Bomber(Unit):
    def _init_(self):
        Unit.__init__(self, 2, 4, 1, 6, "Bomber")


class Submarine(Unit):
    def __init__(self):
        Unit.__init__(self, 1, 2, 1, 4, "Submarine")


class Destroyer(Unit):
    def __init__(self):
        Unit.__init__(self, 2, 2, 2, 4, "Destroyer")


class Cruiser(Unit):
    def _init_(self):
        Unit.__init__(self, 3, 3, 3, 4, "Cruiser")


class AircraftCarrier(Unit):
    def __init__(self):
        Unit.__init__(self, 3, 1, 2, 4, "Aircraft Carrier")


class BattleShip(Unit):
    def __init__(self):
        Unit.__init__(self, 8, 4, 4, 6, "Battleship")
