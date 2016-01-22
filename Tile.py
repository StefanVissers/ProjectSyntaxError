__author__ = 'Jamal'
import pygame
from random import *
offset = 50

testlist = []

class Tile:
    def __init__(self, tilex, tiley, income, PlayerNR):
        self.Position = Vector2(tilex, tiley)
        self.income = income
        self.Player = PlayerNR
        self.Traversable = True
        self.Rectangle = pygame.Rect(self.Position.x * offset, self.Position.y  * offset, offset, offset)

class RiverTile:
    def __init__(self, Rtilex, Rtiley):
        self.Position = Vector2(Rtilex, Rtiley)
        self.Traversable = False
        self.Rectangle = pygame.Rect(self.Position.x * offset, self.Position.y  * offset, offset, offset)



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

def create_Map(l):
    for T in l:
        if T == Tile:
            MapTile = Tile(T.Position.x, T.Position.y, T.income, T.Player)
            Map.append(MapTile)
        if T == RiverTile:
            MapRiverTile = RiverTile(T.Position.x, T.Position.y)
            Map.append(MapRiverTile)
    return Map

Map = create_Tilelist()
create_Map(Map)
print(create_Tilelist())
