__author__ = 'stefan'
import Tile
import pygame

main_surface = pygame.display.set_mode((1200, 900))


class Unit:
    def Move(self):
        pass

class Base:
    def __init__(self, player):
        self.Player = player
        self.Health = 25
        self.Money = 500
        self.Barack = BarackObama(player)
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_brown.png'), (50, 50))
        elif player == 2:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_red.png'), (50, 50))
        elif player == 3:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_blue.png'), (50, 50))
        else:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_green.png'), (50, 50))


class BarackObama:
    def __init__(self, player):
        self.Player = player
        self.Health = 5
        self.Name = "Barack"
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/brown_tent.png'), (45, 45))
        elif player == 2:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/red_tent.png'), (45, 45))
        elif player == 3:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/blue_tent.png'), (45, 45))
        else:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/green_tent.png'), (45, 45))


class Soldier:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Cost = 150
        self.Health = 1
        self.Attack = 1
        self.Name = "Soldier"
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/soldier1.png'), (45, 45))
        elif player == 2:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/soldier2.png'), (45, 45))
        elif player == 3:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/soldier3.png'), (45, 45))
        else:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/soldier4.png'), (45, 45))

class Robot:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Cost = 300
        self.Health = 2
        self.Attack = 25
        self.Name = "Robot"
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/robot1.png'), (45, 45))
        elif player == 2:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/robot2.png'), (45, 45))
        elif player == 3:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/robot3.png'), (45, 45))
        else:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/robot4.png'), (45, 45))

class Tank:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Cost = 750
        self.Health = 2
        self.Attack = 2
        self.Name = "Tank"
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/tank1.png'), (45, 45))
        elif player == 2:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/tank2.png'), (45, 45))
        elif player == 3:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/tank3.png'), (45, 45))
        else:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/tank4.png'), (45, 45))

class Boat:
    def __init__(self, player):
        self.Unit = Unit
        self.Player = player
        self.Cost = 1000
        self.Health = 1
        self.Attack = 0
        self.Soldier = []
        self.Robot = []
        self.Tank = []
        self.Name = "Boat"
        if player == 1:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/boat1.png'), (45, 45))
        elif player == 2:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/boat2.png'), (45, 45))
        elif player == 3:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/boat3.png'), (45, 45))
        else:
            self.Texture = pygame.transform.scale(pygame.image.load('Pics/units/boat4.png'), (45, 45))

