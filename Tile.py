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

#playernr = randint(0,3)

#WoestijnTile = Tile(0, 16, 50, 0)
#IJsTile = Tile(17, 0, 50, 1)
#BosTile = Tile(17, 16, 50, 2)
#MoerasTile = Tile(0, 0, 50, 3)



def create_Tilelist():
    list = []
    x = 0
    y = 0
    for a in range(0,17):
        for b in range(0,17):
            if a == 6 and b >= 5 and y <= 12:
                list.append(RiverTile(x, y))
            if a == 5 and b >= 6 and y <= 11:
                list.append(RiverTile(x, y))
            if a == 11 and y >= 5 and y <= 12:
                list.append(RiverTile(x, y))
            if a == 12 and y >= 6 and y <= 12:
                list.append(RiverTile(x, y))
            if a >= 0 and a <= 4 and y >= 7 and y <= 10:
                list.append(RiverTile(x, y))
            if a >= 7 and a <= 10 and b >= 0 and b <= 6:
                list.append(RiverTile(x, y))
            if a >= 7 and a <= 10 and b >= 0 and b <= 6:
                list.append(RiverTile(x, y))
            if a >= 13 and a <= 17 and b >= 7 and b <= 10:
                list.append(RiverTile(x, y))
            if a >= 7 and a <= 10 and b >= 11 and b <= 17:
                list.append((RiverTile(x, y)))
            else:
                list.append(Tile(x, y, 50, 0))
            y += 1
        y = 0
        x += 1
    return list



create_Tilelist()
print(create_Tilelist())
print("Hello world")