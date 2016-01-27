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

#TODO Change Tile.Barack Boolean at cursor

def placeUnit(clickedtile): #TODO Add unit to unitcount at clicked tile
    for i in Map:
        unit = UnitClasses.Tank(None, i)
        clickedtile.Unitcount.append(unit)
        return unit

# def drawUnits(army): #TODO Draw unit if a Tile.unitcount > 0
#     for i in army:
#         if i is not None:
#             main_surface.blit(i.Texture, (i.Tile.Position.x * 50 + 3, i.Tile.Position.y * 50 + 3))


#TODO Create a function through which as a player i can see the unitcount on any given tile



def SelectedUnit(event, mouse_pos): #TODO Create a submenu which the player can access after choosing "Buy a unit" in which the player can choose between units
    for ev in event:
        if ev.type == pygame.MOUSEBUTTONDOWN and shopmenusubButton1.collidepoint(mouse_pos):
            return Soldier
        if ev.type == pygame.MOUSEBUTTONDOWN and shopmenusubButton2.collidepoint(mouse_pos):
            return Robot
        if ev.type == pygame.MOUSEBUTTONDOWN and shopmenusubButton3.collidepoint(mouse_pos):
            return Tank
        if ev.type == pygame.MOUSEBUTTONDOWN and shopmenusubButton4.collidepoint(mouse_pos):
            return Boat

# def createArmylist(clickedtile, SelectedUnit):
#     unit = UnitClasses.SelectedUnit.append(unit)
#     clickedtile.Unitcount.append(unit)
#     return clickedtile


# def clickTile(event, mouse_pos):
#     global clickedtiles
#     clickedtiles = []
#     for ev in event:
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#             for i in Map:
#                 if i.Rectangle.collidepoint(mouse_pos):
#                     clickedtiles.append(i)
#                     print(i.Position.x, i.Position.y, i.Traversable)
#     return clickedtiles