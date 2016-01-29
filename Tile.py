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
        self.Base = False
        self.Soldier = []
        self.Tank = []
        self.Robot = []
        self.Boat = []

class Vector2:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

def drawBase(Map):
    for i in Map:
        if i.Position.x == 0 and i.Position.y == 0:
            i.Base = True
            if i.Base == True:
                Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_green.png'), (50,50))
                main_surface.blit((Texture), (i.Position.x * offset, i.Position.y * offset))
        if i.Position.x == 17 and i.Position.y == 0:
            i.Base = True
            if i.Base == True:
                Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_blue.png'), (50,50))
                main_surface.blit((Texture), (i.Position.x * offset, i.Position.y * offset))
        if i.Position.x == 0 and i.Position.y == 17:
            i.Base = True
            if i.Base == True:
                Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_red.png'), (50,50))
                main_surface.blit((Texture), (i.Position.x * offset, i.Position.y * offset))
        if i.Position.x == 17 and i.Position.y == 17:
            i.Base = True
            if i.Base == True:
                Texture = pygame.transform.scale(pygame.image.load('Pics/units/castle_brown.png'), (50,50))
                main_surface.blit((Texture), (i.Position.x * offset, i.Position.y * offset))


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

def countUnits(coordinates, Map):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                a = len(i.Soldier)
                b = len(i.Tank)
                c = len(i.Robot)
                d = len(i.Boat)
                print(str(a) + " Soldier(s)")
                print(str(b) + " Tank(s)")
                print(str(c) + " Robot(s)")
                print(str(d) + " Boat(s)")
                print(i.Barack)


def countSoldiers(coordinates, Map):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                a = len(i.Soldier)
                return "Soldiers : " + str(a)

def countTanks(coordinates, Map):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                b = len(i.Tank)
                return "Tanks : " + str(b)

def countRobots(coordinates, Map):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                c = len(i.Robot)
                return "Robots : " + str(c)

def countBoats(coordinates, Map):
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                d = len(i.Boat)
                return "Boats : " + str(d)

def drawMoney(startmoney):
    #moneydisplay = pygame.Rect(1100, 500, 200, 50)
    font = pygame.font.SysFont(None, 40)
    Moneytext = font.render("Money : " + str(startmoney), 1, (255, 255, 255))
    #main_surface.fill((0, 0 , 0), (moneydisplay))
    main_surface.blit(Moneytext, (950, 600))


def drawUnits(map, a):
    for x in map:
        if x.Barack == True and a == 1:
            main_surface.blit(pygame.transform.scale(pygame.image.load('Pics/units/blue_tent.png'), (45, 45)), (x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        if x.Barack == True and a == 2:
            main_surface.blit(pygame.transform.scale(pygame.image.load('Pics/units/blue_tent.png'), (45, 45)), (x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        if x.Barack == True and a == 3:
            main_surface.blit(pygame.transform.scale(pygame.image.load('Pics/units/blue_tent.png'), (45, 45)), (x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        if x.Barack == True and a == 4:
            main_surface.blit(pygame.transform.scale(pygame.image.load('Pics/units/blue_tent.png'), (45, 45)), (x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        if x.Barack == True and x.Base == True:
            main_surface.blit(UnitClasses.Base.Texture)
        for u in x.Soldier:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Tank:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Robot:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Boat:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))


def selectUnit(coordinates1, coordinates2, Map):
    #Units op land verplaatsen
    if coordinates1 is not None:
        #Kijkt of de coordinaten naast de oorspronkelijke Tile zit en of deze geen rivier is
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable):
            for i in Map:
                #kijkt waar de 1e coordinaat is en kijkt of er een unit op staat
                if coordinates1.Position.x == i.Position.x and coordinates1.Position.y == i.Position.y and i.Soldier is not [] and i.Tank is not [] and i.Robot is not []:
                    #Verplaatst de units van de tile naar een tijdelijke lijst en leegt de tile unit lijsten
                    MovelistSoldier = i.Soldier
                    MovelistTank = i.Tank
                    MovelistRobot = i.Robot
                    i.Soldier = []
                    i.Tank = []
                    i.Robot = []

    if coordinates2 is not None:
        #Kijkt of de coordinaten naast de oorspronkelijke Tile zit en of deze geen rivier is
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable):
            for i in Map:
                #Kijkt waar het 2e coordinaat zit
                if coordinates2.Position.x == i.Position.x and coordinates2.Position.y == i.Position.y:
                    #Verplaatst de units van de tijdelijke lijst naar het 2e coordinaat
                    for x in MovelistSoldier:
                        i.Soldier.append(x)
                    for x in MovelistTank:
                        i.Tank.append(x)
                    for x in MovelistRobot:
                        i.Robot.append(x)

    #Boot units laden
    if coordinates1 is not None:
        #Kijkt of de coordinaten naast de oorspronkelijke Tile zit
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x):
            for i in Map:
                #Kijkt of de eerste tile land is en de tweede tile een rivier is
                if coordinates1.Position.x == i.Position.x and coordinates1.Position.y == i.Position.y and coordinates1.Traversable and coordinates2.Traversable == False:
                    #Kijkt of er op de rivier een boot zit en op het land een unit staat
                    if coordinates2.Boat and (coordinates1.Soldier or coordinates1.Tank or coordinates1.Robot):
                        #Verplaatst de units van het land naar een tijdelijke lijst
                        MovelistSoldier = i.Soldier
                        MovelistTank = i.Tank
                        MovelistRobot = i.Robot


    if coordinates2 is not None:
        #Kijkt of de coordinaten naast de oorspronkelijke Tile zit
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x):
            for i in Map:
                #Kijkt waar de eerste coordinaten zitten en kijkt of de eerste land is en de tweede rivier
                if coordinates1.Position.x == i.Position.x and coordinates1.Position.y == i.Position.y and coordinates1.Traversable and coordinates2.Traversable == False:
                    #Kijkt of er op de rivier een boot zit en op het land een unit staat
                    if coordinates2.Boat and (coordinates1.Soldier or coordinates1.Tank or coordinates1.Robot):
                        #Verplaatst de units van de tijdelijke lijst naar de unitslijsten in de boot en leegt de lijsten van units van het land
                        for x in MovelistSoldier:
                            coordinates2.Boat[0].Soldier.append(x)
                        for x in MovelistTank:
                            coordinates2.Boat[0].Tank.append(x)
                        for x in MovelistRobot:
                            coordinates2.Boat[0].Robot.append(x)
                        i.Soldier = []
                        i.Tank = []
                        i.Robot = []

    #Boot Units uitladen
    if coordinates1 is not None:
        #Kijkt of de coordinaten naast de oorspronkelijke Tile zit
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x):
            for i in Map:
                #Kijkt of de Eerste cooridnaat een Rivier is en het tweede coordinaat land is.
                if coordinates1.Position.x == i.Position.x and coordinates1.Position.y == i.Position.y and coordinates1.Traversable == False and coordinates2.Traversable:
                    #Kijkt of er units in de boot zitten en verplaatst deze dan naar een Tijdelijke lijst
                    if coordinates1.Boat and (coordinates1.Boat[0].Soldier or coordinates1.Boat[0].Tank or coordinates1.Boat[0].Robot):
                        MovelistSoldier = i.Boat[0].Soldier
                        MovelistTank = i.Boat[0].Tank
                        MovelistRobot = i.Boat[0].Robot

    if coordinates2 is not None:
        #Kijkt of de coordinaten naast de oorspronkelijke Tile zit
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x):
            for i in Map:
                #Kijkt of de eerste Tile een rivier is en de tweede land is, en waar de coordinaten zitten
                if coordinates2.Position.x == i.Position.x and coordinates2.Position.y == i.Position.y and coordinates1.Traversable == False and coordinates2.Traversable:
                    #kijkt of de boot units in zich heeft en het tweede coordinaat geen boot opzich heeft
                    #Vervolgens Plaatst hij de units op het land en leegt de boot zijn unitlijsten
                    if not coordinates2.Boat and (coordinates1.Boat[0].Soldier or coordinates1.Boat[0].Tank or coordinates1.Boat[0].Robot):
                        for x in MovelistSoldier:
                            coordinates2.Soldier.append(x)
                        for x in MovelistTank:
                            coordinates2.Tank.append(x)
                        for x in MovelistRobot:
                            coordinates2.Robot.append(x)
                        coordinates1.Boat[0].Soldier = []
                        coordinates1.Boat[0].Tank = []
                        coordinates1.Boat[0].Robot = []

    #units op water verplaatsen
    if coordinates1 is not None:
        #Kijkt of het 2e coordinaat, zorgt ervoor dat de units op het water blijven en er niet vanaf kunnen komen.
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable == False)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable == False)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable == False)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable == False):
            for i in Map:
                #Doet de boot in een Temporary list, en leegt de Boat lijst van de Tile waar hij weg van gaat
                if coordinates1.Position.x == i.Position.x and coordinates1.Position.y == i.Position.y and coordinates1.Boat is not []:
                    MovelistBoat = i.Boat
                    i.Boat = []

    if coordinates2 is not None:
        #Kijkt of het 2e coordinaat, zorgt ervoor dat de units op het water blijven en er niet vanaf kunnen komen.
        if (coordinates1.Position.x + 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable == False)\
                or (coordinates1.Position.x - 1 == coordinates2.Position.x and coordinates1.Position.y == coordinates2.Position.y and coordinates2.Traversable == False)\
                or (coordinates1.Position.y + 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable == False)\
                or (coordinates1.Position.y - 1 == coordinates2.Position.y and coordinates1.Position.x == coordinates2.Position.x and coordinates2.Traversable == False):
            for i in Map:
                #Doet de boot vanuit de Temporary list naar de Boat lijst van het Coordinaat waar de boot heen wilt
                if coordinates2.Position.x == i.Position.x and coordinates2.Position.y == i.Position.y:
                    for x in MovelistBoat:
                        i.Boat.append(x)

def turn(x):
    x += 1
    if x > 4:
        x = 1
        return x
    return x