__author__ = 'Jamal'
import pygame
from random import *
from Spelbord import *
import UnitClasses
main_surface = pygame.display.set_mode((1200, 900))
offset = 50

class Tile:
    def __init__(self, tilex, tiley, income, playerNR, traversable):
        self.Position = Vector2(tilex, tiley)
        self.Income = income
        self.Player = playerNR
        self.Traversable = traversable
        self.Rectangle = pygame.Rect(self.Position.x * offset, self.Position.y  * offset, offset, offset)
        self.Barack = False
        self.Soldier = []
        self.Tank = []
        self.Robot = []
        self.Boat = []

class Vector2:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y


def create_Tilelist():
    list = []
    for x in range(0,18):
        for y in range(0,18):
            if x == 5 and y >= 6 and y <= 11:
              list.append(Tile(x, y, None, None, False))
            elif x == 6 and y >= 5 and y <= 12:
                list.append(Tile(x, y, None, None, False))
            elif x == 11 and y >= 5 and y <= 12:
                list.append(Tile(x, y, None, None, False))
            elif x == 12 and y >= 6 and y <= 11:
                list.append(Tile(x, y, None, None, False))
            elif x >= 0 and x <= 4 and y >= 7 and y <= 10:
                list.append(Tile(x, y, None, None, False))
            elif x >= 7 and x <= 10 and y >= 0 and y <= 6:
                list.append(Tile(x, y, None, None, False))
            elif x >= 7 and x <= 10 and y >= 0 and y <= 6:
                list.append(Tile(x, y, None, None, False))
            elif x >= 13 and x <= 17 and y >= 7 and y <= 10:
                list.append(Tile(x, y, None, None, False))
            elif x >= 7 and x <= 10 and y >= 11 and y <= 17:
                list.append(Tile(x, y, None, None, False))
            else:
                list.append(Tile(x, y, 50, 0, True))
    return list

def getTile(event, mouse_pos, Map):
    click = pygame.mouse.get_pressed()
    for ev in event:
        if ev.type == pygame.MOUSEBUTTONDOWN and click[0] == 1:
            for i in Map:
                if i.Rectangle.collidepoint(mouse_pos):
                    print(i.Position.x, i.Position.y, i.Traversable)
                    return i


#TODO Create a function through which as a player i can see the unitcount on any given tile
def countUnits(coordinates, Map):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                a = len(i.Soldier)
                b = len(i.Tank)
                c = len(i.Robot)
                d = len(i.Boat)
                print(str(a) + " Soldiers")
                print(str(b) + " Tanks")
                print(str(c) + " Robots")
                print(str(d) + " Boats")
                print(i.Barack)

def drawUnits(map):
    for x in map:
        if x.Barack == True:
            main_surface.blit(pygame.transform.scale(pygame.image.load('Pics/units/flag.png'), (45, 45)), (x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Soldier:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Tank:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Robot:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Boat:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))


#TODO Create a function through which the player can select the tile.unitcount
#TODO Create a function through which the player can move the selected unit through the use of passing the Tile.unitcount to another Tile
def selectUnit(coordinates1, coordinates2, Map):
    if coordinates1 is not None:
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x):
            for i in Map:
                if coordinates1.Position.x == i.Position.x and coordinates1.Position.y == i.Position.y and i.Soldier is not [] and i.Tank is not [] and i.Robot is not []:
                    MovelistSoldier = i.Soldier
                    MovelistTank = i.Tank
                    MovelistBoat = i.Boat
                    MovelistRobot = i.Robot
                    i.Soldier = []
                    i.Tank = []
                    i.Boat = []
                    i.Robot = []

    if coordinates2 is not None:
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x):
            for i in Map:
                if coordinates2.Position.x == i.Position.x and coordinates2.Position.y == i.Position.y:
                    i.Soldier = MovelistSoldier
                    i.Tank = MovelistTank
                    i.Boat = MovelistBoat
                    i.Robot = MovelistRobot


#TODO Create a submenu which the player can access after choosing "Buy a unit" in which the player can choose between units