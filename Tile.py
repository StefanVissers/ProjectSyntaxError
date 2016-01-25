__author__ = 'Jamal'
import pygame
from random import *

offset = 50



class Tile:
    def __init__(self, tilex, tiley, income, playerNR, traversable):
        self.Position = Vector2(tilex, tiley)
        self.Income = income
        self.Player = playerNR
        self.Traversable = traversable
        self.Rectangle = pygame.Rect(self.Position.x * offset, self.Position.y  * offset, offset, offset)
        self.Unitcount = 0

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
            if x == 6 and y >= 5 and y <= 12:
                list.append(Tile(x, y, None, None, False))
            if x == 11 and y >= 5 and y <= 12:
                list.append(Tile(x, y, None, None, False))
            if x == 12 and y >= 6 and y <= 12:
                list.append(Tile(x, y, None, None, False))
            if x >= 0 and x <= 4 and y >= 7 and y <= 10:
                list.append(Tile(x, y, None, None, False))
            if x >= 7 and x <= 10 and y >= 0 and y <= 6:
                list.append(Tile(x, y, None, None, False))
            if x >= 7 and x <= 10 and y >= 0 and y <= 6:
                list.append(Tile(x, y, None, None, False))
            if x >= 13 and x <= 17 and y >= 7 and y <= 10:
                list.append(Tile(x, y, None, None, False))
            if x >= 7 and x <= 10 and y >= 11 and y <= 17:
                list.append(Tile(x, y, None, None, False))
            else:
                list.append(Tile(x, y, 50, 0, True))
    return list

Map = create_Tilelist()

print (Map[1])

def clickOnTile():
    ev = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in ev:
        if event == pygame.MOUSEBUTTONDOWN:
            for i in Map:
                if i.Rectangle.collidepoint(mouse_pos):
                    print ("Yay")

0x02E58350