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
        self.Unitcount = []

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

Map = create_Tilelist()

def getTile(event, mouse_pos):
    click = pygame.mouse.get_pressed()
    for ev in event:
        if ev.type == pygame.MOUSEBUTTONDOWN and click[0] == 1:
            for i in Map:
                if i.Rectangle.collidepoint(mouse_pos):
                    print(i.Position.x, i.Position.y, i.Traversable)
                    return i



def placeUnit(clickedtile): #TODO Add unit to unitcount at clicked tile
    for i in Map:
        unit = UnitClasses.Tank(None, i)
        clickedtile.Unitcount.append(unit)
        return unit


#TODO Create a function through which as a player i can see the unitcount on any given tile
def viewunitcount(coordinates):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                a = (i.Unitcount.count(UnitClasses.BarackObama))
                return a
#TODO Create a submenu which the player can access after choosing "Buy a unit" in which the player can choose between units


def SpawnBarack(coordinates, army, klik):
    if coordinates is not None and klik is not 1:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable and i.Barack == False:
                unit = UnitClasses.BarackObama(None, i)
                army.append(unit)
                i.Unitcount.append(unit)
                i.Barack = True


def drawUnits(units):
    for u in units:
        main_surface.blit(u.Texture,(u.Tile.Position.x * 50 + 3, u.Tile.Position.y * 50 + 3, 45, 45))

#TODO Create a function through which the player can select the tile.unitcount, highlight the selected Tile

#TODO Create a function through which the player can move the selected unit through the use of passing the Tile.unitcount to another Tile

