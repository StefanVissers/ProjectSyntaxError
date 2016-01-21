__author__ = 'Jamal'

#from random import *

class Tile:
    def __init__(self, tilex, tiley, income, playernumber):
        self.position = Vector2(tilex, tiley)
        self.income = income
        self.traversable = True
        self.pnumber = playernumber


class Vector2:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

#playernr = randint(0,3)

#WoestijnTile = Tile(0, 16, 50, 0)
#IJsTile = Tile(17, 0, 50, 1)
#BosTile = Tile(17, 16, 50, 2)
#MoerasTile = Tile(0, 0, 50, 3)


Tiles = []
def create_tilelist(list):
    x = 0
    y = 0
    for a in range(0,17):
        for b in range(0,17):
            list.append(Tile(x, y, 50, 0))
            y += 1
            if
        y = 0
        x += 1
    return list



create_tilelist(Tiles)
print (create_tilelist(Tiles))