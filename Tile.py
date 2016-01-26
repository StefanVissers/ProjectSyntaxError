__author__ = 'Jamal'
import pygame
from random import *
from Spelbord import *
import UnitClasses
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

def clickTile(event, mouse_pos, bordload, quitingamepng):
    click = pygame.mouse.get_pressed()
    for ev in event:
        if ev.type == pygame.MOUSEBUTTONDOWN and click[0]==1:
            for i in Map:
                if i.Rectangle.collidepoint(mouse_pos):
                    print(i.Position.x, i.Position.y, i.Traversable)
                    if i.Position.x == 0 and i.Position.y == 0:
                        print ("BASE 1")
                        shopMenu(pygame.display.set_mode((1200, 900)), bordload, quitingamepng, event, mouse_pos)

def shopMenu(main_surface, bordload, quitingamepng, event, mouse_pos):
    font = pygame.font.SysFont("Courier", 20)
    shopmenuButton1Text = font.render("Buy a Soldier! " + str(150 ), 1, (255,255,0))
    balancetext = font.render("Balance: " + str(800), 1, (255,255,0))
    menuLayout = pygame.Rect(900, 650, 500, 300)
    shopmenuButton1 = pygame.Rect(900, 700, 500, 50)
    shopmenuButton2 = pygame.Rect(900, 750, 500, 50)
    shopmenuButton3 = pygame.Rect(900, 800, 500, 50)
    background = pygame.image.load('Pics/Background.jpg')
    main_surface.blit(background, (0, 0))
    main_surface.fill((255, 0, 0), (menuLayout))
    main_surface.fill((0, 255, 0), (shopmenuButton1))
    main_surface.fill((0, 0, 255), (shopmenuButton2))
    main_surface.fill((255, 255, 0), (shopmenuButton3))
    main_surface.blit(shopmenuButton1Text, (900, 700))
    main_surface.blit(balancetext, (900, 850))
    main_surface.blit(bordload, (0, 0))
    main_surface.blit(quitingamepng, (900, 0))
    for ev in event:
        if ev.type == pygame.MOUSEBUTTONDOWN and shopmenuButton1.collidepoint(mouse_pos):
            print ("SPAWN UNIT")

