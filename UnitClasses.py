__author__ = 'stefan'
from Tile import *
import pygame

main_surface = pygame.display.set_mode((1200, 900))

class Unit:
    def Move(self):
        pass

class Soldier:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 150
        self.Health = 1
        self.Attack = 1

class Robot:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 300
        self.Health = 2
        self.Attack = 2

class Tank:
    def __init__(self, player, tile, textuur):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 750
        self.Health = 2
        self.Attack = 2
        self.Texture = pygame.transform.scale(pygame.image.load('Pics/monster1.png'),(45,45))

class Boat:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 1000
        self.Health = 1
        self.Attack = 0
        self.Units = []


def drawUnits(army):
    for i in army:
        main_surface.blit(i.Texture,(i.Tile.Position.x * 50 + 3, i.Tile.Position.y * 50 + 3, 45, 45))




print ("Hello")