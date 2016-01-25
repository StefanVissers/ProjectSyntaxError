__author__ = 'stefan'
import Tile

class Unit:
    def Move(self):
        pass

class Soldier:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Tile = Tile
        self.Cost = 150
        self.Health = 1
        self.Attack = 1

class Robot:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Tile = Tile
        self.Cost = 300
        self.Health = 2
        self.Attack = 2

class Tank:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Tile = Tile
        self.Cost = 750
        self.Health = 2
        self.Attack = 2

class Boat:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Tile = Tile
        self.Cost = 1000
        self.Health = 1
        self.Attack = 0
        self.Units = []
