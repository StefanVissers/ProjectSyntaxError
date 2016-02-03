__author__ = 'Jamal'
import pygame
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
        self.BarackObama = []
        self.Bases = []


class Vector2:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y


def drawBase(Map):
    for i in Map:
        if i.Position.x == 0 and i.Position.y == 0:
            i.Base = True
            if i.Base == True:
                i.Bases.append(UnitClasses.Base(4))
        if i.Position.x == 17 and i.Position.y == 0:
            i.Base = True
            if i.Base == True:
                i.Bases.append(UnitClasses.Base(3))
        if i.Position.x == 0 and i.Position.y == 17:
            i.Base = True
            if i.Base == True:
                i.Bases.append(UnitClasses.Base(2))
        if i.Position.x == 17 and i.Position.y == 17:
            i.Base = True
            if i.Base == True:
                i.Bases.append(UnitClasses.Base(1))


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

def HealthSoldier(coordinates, Map):
    HealthSoldier = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Soldier is not []:
                    for i in range(len(i.Soldier)):
                        HealthSoldier += 1
                return HealthSoldier

def HealthTank(coordinates, Map):
    HealthTank = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Tank is not []:
                    for i in range(len(i.Tank)):
                        HealthTank += 3
                return HealthTank

def HealthRobot(coordinates, Map):
    HealthRobot = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Robot is not []:
                    for i in range(len(i.Robot)):
                        HealthRobot += 2
                return HealthRobot

def HealthBoat(coordinates, Map):
    HealthBoat = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Boat is not []:
                    for i in range(len(i.Boat)):
                        HealthBoat += 2
                return HealthBoat

def HealthBase(coordinates, Map, players):
    HealthBase = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Bases is not []:
                    for i in i.Bases:
                        for d in players:
                            if d.Player == i.Player:
                                return d.Health
        return 0

def HealthBarack(coordinates, Map):
    HealthBarack = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.BarackObama is not []:
                    for i in range(len(i.BarackObama)):
                        HealthBarack += 5
                return HealthBarack

def DMGSoldier (coordinates, Map):
    DMGSoldier = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Soldier is not []:
                    for i in range(len(i.Soldier)):
                        DMGSoldier += 1
                return DMGSoldier

def DMGTank (coordinates, Map):
    DMGTank = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Tank is not []:
                    for i in range(len(i.Tank)):
                        DMGTank += 3
                return DMGTank

def DMGRobot (coordinates, Map):
    DMGRobot = 0
    if coordinates is not None:
        for i in Map:
            if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y:
                if i.Robot is not []:
                    for i in range(len(i.Robot)):
                        DMGRobot += 2
                return DMGRobot

def drawMoney(startmoney):
    #moneydisplay = pygame.Rect(1100, 500, 200, 50)
    font = pygame.font.SysFont(None, 40)
    Moneytext = font.render("Money : " + str(startmoney), 1, (255, 255, 255))
    #main_surface.fill((0, 0 , 0), (moneydisplay))
    main_surface.blit(Moneytext, (970, 260))


def drawUnits(map):
    for x in map:
        for u in x.Bases:
            main_surface.blit((u.Texture), (x.Position.x * offset, x.Position.y * offset))
        for u in x.BarackObama:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Soldier:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Tank:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Robot:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))
        for u in x.Boat:
            main_surface.blit(u.Texture,(x.Position.x * 50 + 3, x.Position.y * 50 + 3, 45, 45))

def selectUnit(coordinates1, coordinates2, Map, currentplayer, players):
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

    #Het Vechten van de units
    if coordinates2.Soldier is not None or coordinates2.Robot is not None or coordinates2.Tank is not None:
        player1soldiers = 0
        player2soldiers = 0
        player3soldiers = 0
        player4soldiers = 0
        player1tanks = 0
        player2tanks = 0
        player3tanks = 0
        player4tanks = 0
        player1robots = 0
        player2robots = 0
        player3robots = 0
        player4robots = 0

        for x in coordinates2.Soldier:
            if x.Player == 1:
                player1soldiers += 1
            elif x.Player == 2:
                player2soldiers += 1
            elif x.Player == 3:
                player3soldiers += 1
            elif x.Player == 4:
                player4soldiers += 1

        for x in coordinates2.Tank:
            if x.Player == 1:
                player1tanks += 3
            elif x.Player == 2:
                player2tanks += 3
            elif x.Player == 3:
                player3tanks += 3
            elif x.Player == 4 :
                player4tanks += 3

        for x in coordinates2.Robot:
            if x.Player == 1:
                player1robots += 2
            elif x.Player == 2:
                player2robots += 2
            elif x.Player == 3:
                player3robots += 2
            elif x.Player == 4:
                player4robots += 2

        totalATKplayer_1 = player1soldiers + player1tanks + player1robots
        totalATKplayer_2 = player2soldiers + player2tanks + player2robots
        totalATKplayer_3 = player3soldiers + player3tanks + player3robots
        totalATKplayer_4 = player4soldiers + player4tanks + player4robots
        totalDEFplayer_1 = player1soldiers + player1tanks + player1robots
        totalDEFplayer_2 = player2soldiers + player2tanks + player2robots
        totalDEFplayer_3 = player3soldiers + player3tanks + player3robots
        totalDEFplayer_4 = player4soldiers + player4tanks + player4robots
        newList = []

        #PLAYER 1 VS
        if totalATKplayer_1 > totalDEFplayer_2 and totalDEFplayer_2 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        elif totalATKplayer_1 > totalDEFplayer_3 and totalDEFplayer_3 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        elif totalATKplayer_1 > totalDEFplayer_4 and totalDEFplayer_4 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 1:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        #PLAYER 2 VS
        elif totalATKplayer_2 > totalDEFplayer_1 and totalDEFplayer_1 != 0:
             for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
             coordinates2.Soldier = newList
             newList = []
             for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
             coordinates2.Tank = newList
             newList = []
             for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
             coordinates2.Robot = newList
             newList = []

        elif totalATKplayer_2 > totalDEFplayer_3 and totalDEFplayer_3 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
                coordinates2.Soldier = newList
                newList = []
            for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
                coordinates2.Tank = newList
                newList = []
            for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
                coordinates2.Robot = newList
                newList = []

        elif totalATKplayer_2 > totalDEFplayer_4 and totalDEFplayer_4 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
                coordinates2.Soldier = newList
                newList = []
            for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
                coordinates2.Tank = newList
                newList = []
            for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
                coordinates2.Robot = newList
                newList = []


        #PLAYER 3 VS
        elif totalATKplayer_3 > totalDEFplayer_1 and totalDEFplayer_1 != 0:
             for x in coordinates2.Soldier:
                if x.Player == 3:
                    newList.append(x)
             coordinates2.Soldier = newList
             newList = []
             for x in coordinates2.Tank:
                if x.Player == 3:
                    newList.append(x)
             coordinates2.Tank = newList
             newList = []
             for x in coordinates2.Robot:
                if x.Player == 3:
                    newList.append(x)
             coordinates2.Robot = newList
             newList = []

        elif totalATKplayer_3 > totalDEFplayer_2 and totalDEFplayer_2 !=0:
            for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        elif totalATKplayer_3 > totalDEFplayer_4 and totalDEFplayer_4 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        elif totalATKplayer_4 > totalDEFplayer_1 and totalDEFplayer_1 != 0:
             for x in coordinates2.Soldier:
                if x.Player == 1:
                    newList.append(x)
             coordinates2.Soldier = newList
             newList = []
             for x in coordinates2.Tank:
                if x.Player == 1:
                    newList.append(x)
             coordinates2.Tank = newList
             newList = []
             for x in coordinates2.Robot:
                if x.Player == 1:
                    newList.append(x)
             coordinates2.Robot = newList
             newList = []

        elif totalATKplayer_4 > totalDEFplayer_2 and totalDEFplayer_2 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        elif totalATKplayer_4 > totalDEFplayer_3 and totalDEFplayer_3 != 0:
            for x in coordinates2.Soldier:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Soldier = newList
            newList = []
            for x in coordinates2.Tank:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Tank = newList
            newList = []
            for x in coordinates2.Robot:
                if x.Player == 2:
                    newList.append(x)
            coordinates2.Robot = newList
            newList = []

        elif (totalATKplayer_1 == totalDEFplayer_2 or totalATKplayer_1 == totalDEFplayer_3 or totalATKplayer_1 == totalDEFplayer_4\
                or totalATKplayer_2 == totalDEFplayer_1 or totalATKplayer_2 == totalDEFplayer_3 or totalATKplayer_2 == totalDEFplayer_4\
                or totalATKplayer_3 == totalDEFplayer_1 or totalATKplayer_3 == totalDEFplayer_2 or totalATKplayer_3 == totalDEFplayer_4\
                or totalDEFplayer_4 == totalDEFplayer_1 or totalATKplayer_4 == totalDEFplayer_2 or totalATKplayer_4 == totalDEFplayer_3)\
                and (((totalATKplayer_1 != 0 and totalATKplayer_2 != 0) or (totalATKplayer_3 != 0 and totalATKplayer_4 != 0))\
                or ((totalATKplayer_1 != 0 and totalATKplayer_3 != 0) or (totalATKplayer_2 != 0 and totalATKplayer_4 != 0))\
                or ((totalATKplayer_1 != 0 and totalATKplayer_4 != 0) or (totalATKplayer_2 != 0 and totalATKplayer_3 != 0))):
            coordinates2.Soldier = []
            coordinates2.Tank = []
            coordinates2.Robot = []

    if coordinates2.Bases:# and (coordinates1.Soldier or coordinates1.Tank or coordinates1.Robot):
        totalattack = 0
        for i in coordinates2.Robot:
            totalattack += i.Attack
        for i in coordinates2.Soldier:
            totalattack += i.Attack
        for i in coordinates2.Tank:
            totalattack += i.Attack
        if coordinates2.Bases[0].Player != currentplayer.Player:
            playernr = coordinates2.Bases[0].Player
            for u in players:
                print(u.Player)
                if u.Player == playernr:
                    u.Health -= totalattack
                    if u.Health <= 0:
                        for d in players:
                            if d.Health <= 0:
                                deadplayer = d
                                for i in Map:
                                    for u in i.Soldier:
                                        if u.Player == deadplayer.Player:
                                            i.Soldier = []
                                    for u in i.Tank:
                                        if u.Player == deadplayer.Player:
                                            i.Tank = []
                                    for u in i.Robot:
                                        if u.Player == deadplayer.Player:
                                            i.Robot = []
                                    for u in i.Boat:
                                        if u.Player == deadplayer.Player:
                                            i.Boat = []
                                    for u in i.BarackObama:
                                        if u.Player == deadplayer.Player:
                                            i.BarackObama = []
                                    for u in i.Bases:
                                        if u.Player == deadplayer.Player:
                                            i.Bases = []
                                for i in players:
                                    if i.Player == deadplayer.Player:
                                        players.remove(i)
                                        return players
    return players