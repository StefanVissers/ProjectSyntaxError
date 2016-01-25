__author__ = 'stefan'
import Tile
import pygame

main_surface = pygame.display.set_mode((1200, 900))

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

def drawUnits():
    testmonster = pygame.image.load('Pics/monster1.png')
    testmonster = pygame.transform.scale(testmonster, (45, 45))
    for i in range(0, 18):
        for j in range(0, 18):
            main_surface.blit(testmonster, (i * 50 + 3, j * 50 + 3))
    #test_tile = main_surface.fill ((255,0,0), (53, 53, 45, 45))