__author__ = 'Jamal'

#from random import *

class Tile:
    def __init__(self, tilex, tiley, income, PlayerNR):
        self.Position = Vector2(tilex, tiley)
        self.income = income
        self.Player = PlayerNR
        self.Traversable = True

class RiverTile:
    def __init__(self, Rtilex, Rtiley):
        self.Position = Vector2(Rtilex, Rtiley)
        self.Traversable = False



class Vector2:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y


def create_Tilelist():
    list = []
    for x in range(0,18):
        for y in range(0,18):
            if x == 5 and y >= 6 and y <= 11:
              list.append(RiverTile(x, y))
            if x == 6 and y >= 5 and y <= 12:
                list.append(RiverTile(x, y))
            if x == 11 and y >= 5 and y <= 12:
                list.append(RiverTile(x, y))
            if x == 12 and y >= 6 and y <= 12:
                list.append(RiverTile(x, y))
            if x >= 0 and x <= 4 and y >= 7 and y <= 10:
                list.append(RiverTile(x, y))
            if x >= 7 and x <= 10 and y >= 0 and y <= 6:
                list.append(RiverTile(x, y))
            if x >= 7 and x <= 10 and y >= 0 and y <= 6:
                list.append(RiverTile(x, y))
            if x >= 13 and x <= 17 and y >= 7 and y <= 10:
                list.append(RiverTile(x, y))
            if x >= 7 and x <= 10 and y >= 11 and y <= 17:
                list.append((RiverTile(x, y)))
            else:
                list.append(Tile(x, y, 50, 0))
    return list



Map = create_Tilelist()
print(create_Tilelist())
print("Hello world")

class Base:
    def __init__(self, BaseX, BaseY, BaseIncome, Playernr):
        self.Health = 25
        self.Barack = Barack(Playernr)
        self.Position = Tile(BaseX, BaseY, BaseIncome, Playernr)

class Barack:
    def __init__(self, player):
        self.Health = 5
        self.Cost = 500
        self.Player = player
        self.Tile = Tile

Base1 = Base(0, 0, 100, 1)
Base2 = Base(0, 17, 100, 2)
Base3 = Base(17, 0, 100, 3)
Base4 = Base(17, 17, 100, 4)