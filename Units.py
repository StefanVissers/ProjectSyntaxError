
import pygame
main_surface = pygame.display.set_mode((1200, 900))

class soldier():
    cost = 150

    atk_value = 1
    def_value = 1
    move_value = 1
    atk_range = 1

class robot():
    cost = 300
    atk_value = 2
    def_value = 2
    move_value = 1
    atk_range = 1

class tank():
    cost = 750
    atk_value = 2
    def_value = 2
    move_value = 1
    atk_range = 2

class boat():
    cost = 1000
    atk_value = 0
    def_value = 0
    move_value = 2
    #loadUnit = 1
    #maxUnits = 3


def Drawunits():
    main_surface.fill ((255,0,0), (3, 3, 45, 45))


