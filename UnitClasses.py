__author__ = 'stefan'
import Tile
import pygame

main_surface = pygame.display.set_mode((1200, 900))

class Unit:
    def Move(self):
        pass

class Base:
    def __init__(self, player, tile):
        self.Player = player
        self.Tile = tile
        self.Health = 25
        self.Barack = BarackObama(player, tile)
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/flag.png'), (45, 45))

class BarackObama:
    def __init__(self, player, tile):
        self.Player = player
        self.Tile = tile
        self.Health = 5
        self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/flag.png'), (45, 45))
        self.Name = "Barack"

class Soldier:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 150
        self.Health = 1
        self.Attack = 1
        self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/soldier1.png'), (45, 45))
        self.Name = "Soldier"

class Robot:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 300
        self.Health = 2
        self.Attack = 2
        self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/robot1.png'), (45, 45))
        self.Name = "Robot"

class Tank:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 750
        self.Health = 2
        self.Attack = 2
        self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/tank1.png'), (45, 45))
        self.Name = "Tank"

class Boat:
    def __init__(self, player, tile):
        self.Unit = Unit
        self.Player = player
        self.Tile = tile
        self.Cost = 1000
        self.Health = 1
        self.Attack = 0
        self.Units = []
        self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/boat1.png'), (45, 45))
        self.Name = "Boat"

