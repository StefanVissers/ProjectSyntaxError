from Tile import *
from UnitClasses import *
import Menu
import time
import Manual

# Wat kleur variabelen
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0,)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
main_surface = pygame.display.set_mode((1200, 900))                 # zet de resolutie naar de parameters; 1200(x), 900(y) in dit geval
offset = 50
task = None

quit_in_gamebuttonpng = pygame.image.load('Pics/units/quit_game_button.png').convert_alpha()
areyousurepng = pygame.image.load('Pics/areyousure.png').convert_alpha()
bordload = pygame.image.load('Pics/Spelbord_zonderzijkanten.png')
background = pygame.image.load('Pics/Background.jpg')
quitingamebutton = pygame.Rect(950, 0, 200, 50)
manualbuttonrect = pygame.Rect(950, 100 + (50/3) + (50/3), 200, 50)
shop = pygame.Rect(950, 200, 200, 50)
ViewSoldierButton = pygame.Rect(900, 700, 500, 50)
ViewTankButton = pygame.Rect(900, 750, 500, 50)
ViewRobotButton = pygame.Rect(900, 800, 500, 50)
ViewBoatButton = pygame.Rect(900, 850, 500, 50)
shopmenubutton = pygame.image.load('Pics/units/shop_menu_button.png')
moneydisplay = pygame.Rect(1100, 450, 200, 50)
optionsbuttongame = pygame.image.load('Pics/units/options_button_game.png')
manualbuttongame = pygame.image.load('Pics/units/manual_button_game.png')


def spawnbarak(currentplayer, coordinates, i):
    if currentplayer.Money >= 500:
        unit = UnitClasses.BarackObama(currentplayer.Player)
        coordinates.BarackObama.append(unit)
        i.Barack = True
        currentplayer.Money -= 500


def spawnSoldier(currentplayer, coordinates, i):
    if currentplayer.Money >= 150 or (currentplayer.Player == 4 and currentplayer.Money >= 120):
        unit = UnitClasses.Soldier(currentplayer.Player)
        print("De huidige player = "+ str(currentplayer.Player))
        i.Soldier.append(unit)
        if currentplayer.Player == 4:
            currentplayer.Money -= 120
        else:
            currentplayer.Money -= 150

def spawnTank(currentplayer, coordinates, i):
    if currentplayer.Money >= 750 or (currentplayer.Player == 1 and currentplayer.Money >= 600):
        unit = UnitClasses.Tank(currentplayer.Player)
        i.Tank.append(unit)
        if currentplayer.Player == 1:
            currentplayer.Money -= 600
        else:
            currentplayer.Money -= 750

def spawnRobot(currentplayer, coordinates, i):
    if currentplayer.Money >= 300 or (currentplayer.Player == 2 and currentplayer.Money >= 240):
        unit = UnitClasses.Robot(currentplayer.Player)
        i.Robot.append(unit)
        if currentplayer.Player == 2:
            currentplayer.Money -= 240
        else:
            currentplayer.Money -= 300


def reload(Map):                                                       # herinstantieert het bord
    main_surface.blit(background, (0,0))
    main_surface.blit(quit_in_gamebuttonpng, (950, 0))
    main_surface.blit(optionsbuttongame, (950, 50 + (50/3)))
    main_surface.blit(manualbuttongame, (950, 100 + (50/3) + (50/3)))
    main_surface.blit(bordload, (0,0))
    main_surface.blit(shopmenubutton, (950, 200))

def draw_board():
    main_surface.blit(background, (0,0))
    main_surface.blit(quit_in_gamebuttonpng, (950, 0))
    main_surface.blit(optionsbuttongame, (950, 50 + (50/3)))
    main_surface.blit(manualbuttongame, (950, 100 + (50/3)+ (50/3)))
    main_surface.blit(bordload, (0,0))
    main_surface.blit(shopmenubutton, (950, 200))

    klik = 0
    shopmenu = 0
    soldier = 0
    tank = 0
    robot = 0
    boot = 0
    barak = 0
    menu = 0
    testlist = []
    shopmenuimage = pygame.image.load('Pics/units/Shop_menu_unf.png')

    coordinates1 = None
    font = pygame.font.SysFont(None, 25)
    turnfont = pygame.font.SysFont(None, 48)

    Map = Tile.create_Tilelist()
    drawBase(Map)
    zetten = 0
    players = [(Base(1)), (Base(2)), (Base(3)), (Base(4))]
    currentplayer = players[0]
    moneycheck = False
    player = 0

    while True:
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        event = pygame.event.get()            #kan alle events zijn zoals mouse_click
        coordinates = getTile(event, mouse_pos, Map)

        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN and quitingamebutton.collidepoint(mouse_pos):
                klik = 1
            elif ev.type == pygame.QUIT:            # Window close button clicked?
                pygame.quit()
                quit()
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:   # back to main menu
                klik = 1
            elif ev.type == pygame.MOUSEBUTTONDOWN and shop.collidepoint(mouse_pos):
                shopmenu = 1
            elif ev.type == pygame.MOUSEBUTTONDOWN and manualbuttonrect.collidepoint(mouse_pos):
                Manual.manual()
                reload(Map)

        if coordinates is not None:
            # Unit Count TEXT
            soldierCounttext = font.render(str(countSoldiers(coordinates, Map)), 1, (255,255,0))
            main_surface.fill((0, 0 , 0), (ViewSoldierButton))
            main_surface.blit(soldierCounttext, (900, 700))
            tankCounttext = font.render(str(countTanks(coordinates, Map)), 1, (255,0,0))
            main_surface.fill((0, 0 , 0), (ViewTankButton))
            main_surface.blit(tankCounttext, (900, 720))
            robotCounttext = font.render(str(countRobots(coordinates, Map)), 1, (255,50,0))
            main_surface.fill((0, 0 , 0), (ViewRobotButton))
            main_surface.blit(robotCounttext, (900, 740))
            boatCounttext = font.render(str(countBoats(coordinates, Map)), 1, (255,100,0))
            main_surface.fill((0, 0 , 0), (ViewBoatButton))
            main_surface.blit(boatCounttext, (900, 760))

            # Unit Health TEXT
            # Healthtext = font.render(str(countHealth(coordinates, Map)), 1, (255,150,0))
            # main_surface.blit(Healthtext, (900, 780))

        if shopmenu == 1:
            UnitS = pygame.Rect(900, 300, 142, 68)
            UnitT = pygame.Rect(1060, 300, 142, 68)
            UnitR = pygame.Rect(900, 392, 140, 68)
            UnitB = pygame.Rect(1060, 392, 142, 68)
            UnitBr = pygame.Rect(900, 480, 142, 68)
            Back  = pygame.Rect(1059, 480, 142, 68)

            main_surface.blit(shopmenuimage, (900, 300))

            if ev.type == pygame.MOUSEBUTTONDOWN and UnitS.collidepoint(mouse_pos):
                soldier = 1
                shopmenu = 0
                reload(Map)
            elif ev.type == pygame.MOUSEBUTTONDOWN and UnitT.collidepoint(mouse_pos):
                tank = 1
                shopmenu = 0
                reload(Map)
            elif ev.type == pygame.MOUSEBUTTONDOWN and UnitR.collidepoint(mouse_pos):
                robot = 1
                shopmenu = 0
                reload(Map)
            elif ev.type == pygame.MOUSEBUTTONDOWN and UnitB.collidepoint(mouse_pos):
                boot = 1
                shopmenu = 0
                reload(Map)
            elif ev.type == pygame.MOUSEBUTTONDOWN and UnitBr.collidepoint(mouse_pos):
                barak = 1
                shopmenu = 0
                reload(Map)
            elif ev.type == pygame.MOUSEBUTTONDOWN and Back.collidepoint(mouse_pos):
                shopmenu = 0
                reload(Map)


        if not moneycheck:
            for i in Map:
                if len(i.Soldier) > 0:
                    for x in i.Soldier:
                        if x.Player == currentplayer.Player:
                            currentplayer.Money += 50
                elif len(i.Tank) > 0:
                    for x in i.Tank:
                        if x.Player == currentplayer.Player:
                            currentplayer.Money += 50
                elif len(i.Robot) > 0:
                    for x in i.Robot:
                        if x.Player == currentplayer.Player:
                            currentplayer.Money += 50
                elif len(i.Boat) > 0:
                    for x in i.Boat:
                        if x.Player == currentplayer.Player:
                            currentplayer.Money += 50
            moneycheck = True
        drawMoney(currentplayer.Money)


        if barak == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if len(i.Soldier) >= 1 or len(i.Tank) >= 1 or len(i.Robot) >= 1:
                            if len(coordinates.BarackObama) < 1 and i.Base == False:
                                for x in i.Soldier:
                                    if x.Player == currentplayer.Player:
                                        spawnbarak(currentplayer, coordinates, i)
                                        zetten += 1
                                        barak = 0
                                        print("Het aantal zetten = " +str(zetten))
                                    else:
                                        barak = 0
                                for x in i.Tank:
                                    if x.Player == currentplayer.Player:
                                        spawnbarak(currentplayer, coordinates, i)
                                        zetten += 1
                                        barak = 0
                                        print("Het aantal zetten = " +str(zetten))
                                    else:
                                        barak = 0
                                for x in i.Robot:
                                    if x.Player == currentplayer.Player:
                                        spawnbarak(currentplayer, coordinates, i)
                                        zetten += 1
                                        barak = 0
                                        print("Het aantal zetten = " +str(zetten))
                                    else:
                                        barak = 0
                            else:
                                barak = 0



        if soldier == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            for x in i.BarackObama:
                                if x.Player == currentplayer.Player:
                                    spawnSoldier(currentplayer, coordinates, i)
                                    zetten += 1
                                    soldier = 0
                                    print("Het aantal zetten = " +str(zetten))
                                else:
                                    soldier = 0
                            for x in i.Bases:
                                if x.Player == currentplayer.Player:
                                    spawnSoldier(currentplayer, coordinates, i)
                                    zetten += 1
                                    soldier = 0
                                    print("Het aantal zetten = " +str(zetten))
                                else:
                                    soldier = 0
                        else:
                            soldier = 0

        if tank == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            for x in i.BarackObama:
                                if x.Player == currentplayer.Player:
                                    spawnTank(currentplayer, coordinates, i)
                                    zetten += 1
                                    tank = 0
                                    print("Het aantal zetten = " +str(zetten))
                                else:
                                    tank = 0
                            for x in i.Bases:
                                if x.Player == currentplayer.Player:
                                    spawnTank(currentplayer, coordinates, i)
                                    zetten += 1
                                    tank = 0
                                    print("Het aantal zetten = " +str(zetten))
                                else:
                                    tank = 0
                        else:
                            tank = 0

        if robot == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            for x in i.BarackObama:
                                if x.Player == currentplayer.Player:
                                    spawnRobot(currentplayer, coordinates, i)
                                    zetten += 1
                                    robot = 0
                                    print("Het aantal zetten = " +str(zetten))
                                else:
                                    robot = 0
                            for x in i.Bases:
                                if x.Player == currentplayer.Player:
                                    spawnRobot(currentplayer, coordinates, i)
                                    zetten += 1
                                    robot = 0
                                    print("Het aantal zetten = " +str(zetten))
                                else:
                                    robot = 0
                        else:
                            robot = 0

        if boot == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is False:
                        for i in Map:
                            if (coordinates.Position.x + 1 == i.Position.x and coordinates.Position.y == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    or (coordinates.Position.x - 1 == i.Position.x and coordinates.Position.y == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    or (coordinates.Position.x == i.Position.x and coordinates.Position.y + 1 == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    or (coordinates.Position.x == i.Position.x and coordinates.Position.y - 1 == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    and (currentplayer.Money >= 1000 or (currentplayer.Player == 3 and currentplayer.Money >= 800)):
                                unit = UnitClasses.Boat(currentplayer.Player)
                                coordinates.Boat.append(unit)
                                boot = 0
                                zetten += 1
                                if currentplayer.Player == 3:
                                    currentplayer.Money -= 800
                                else:
                                    currentplayer.Money -= 1000
                                print(zetten)

        if coordinates is not None and coordinates1 is None:
            if (coordinates.Soldier != [] or coordinates.Tank != [] or coordinates.Robot != [] or coordinates.Boat != []):
                if len(coordinates.Soldier) > 0:
                    soldiercheck = 0
                    for i in coordinates.Soldier:
                        if i.Player == currentplayer.Player:
                            soldiercheck += 1
                            if soldiercheck == len(coordinates.Soldier):
                                coordinates1 = getTile(event, mouse_pos, Map)
                if len(coordinates.Robot) > 0:
                    robotcheck = 0
                    for i in coordinates.Robot:
                        if i.Player == currentplayer.Player:
                            robotcheck += 1
                            if robotcheck == len(coordinates.Robot):
                                coordinates1 = getTile(event, mouse_pos, Map)
                if len(coordinates.Tank) > 0:
                    tankcheck = 0
                    for i in coordinates.Tank:
                        if i.Player == currentplayer.Player:
                            tankcheck += 1
                            if tankcheck == len(coordinates.Tank):
                                coordinates1 = getTile(event, mouse_pos, Map)
                if len(coordinates.Boat) > 0:
                    boatcheck = 0
                    for i in coordinates.Boat:
                        if i.Player == currentplayer.Player:
                            boatcheck += 1
                            if boatcheck == len(coordinates.Boat):
                                coordinates1 = getTile(event, mouse_pos, Map)

        if coordinates1 != coordinates and coordinates is not None and coordinates1 is not None:
            if (coordinates1.Soldier != [] or coordinates1.Tank != [] or coordinates1.Robot != [] or coordinates1.Boat != []):
                    # print("Deze unit behoort tot player: " + str(coordinates1.Soldier[0].Player))
                    coordinates2 = getTile(event, mouse_pos, Map)
                    players = Tile.selectUnit(coordinates1, coordinates2, Map, currentplayer, players)
                    zetten += 1
                    print("Het aantal zetten = " +str(zetten))
                    coordinates1 = None
                    coordinates2 = None
                    coordinates = None
                    reload(Map)
        drawUnits(Map)

        if zetten >= 4:
            print("De beurt van player " + str(currentplayer.Player) + " is nu voorbij")
            player += 1
            if player > len(players) - 1:
                player = 0
            currentplayer = players[player]
            print("De beurt van player " + str(currentplayer.Player) + " begint nu")
            zetten = 0
            moneycheck = False
            TurnText = turnfont.render("Player " + str(currentplayer.Player) + "'s turn!", 1, (0, 0, 0))
            TurnPNG = pygame.image.load('Pics/units/playerturn_button.png')
            main_surface.blit(TurnPNG, (300, 200))
            main_surface.blit(TurnText, (325, 235))

        if klik == 1:
            main_surface.blit(areyousurepng, (300, 200))
            yesbutton = pygame.Rect(410, 415, 190, 100)    # position yes button
            nobutton = pygame.Rect(630, 415, 190, 100)     # position no button
            if ev.type == pygame.MOUSEBUTTONDOWN and yesbutton.collidepoint(mouse_pos):
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN and nobutton.collidepoint(mouse_pos):
                klik = 2
        elif klik == 2:
            main_surface.blit(bordload, (0,0))
            reload(Map)
            klik = 0

        if currentplayer.Money >= 50000:
            main_surface.fill(BLACK)
            main_surface.blit(pygame.image.load('Pics/winner.png'), (0, 0))
            playertext = font.render(("Player " + str(currentplayer.Player) + " is the winner"), 1, (255,255,255))
            main_surface.blit(playertext, (500, 670))
            escapetext = font.render(("Press esc to go back to main menu"), 1, (255,255,255))
            main_surface.blit(escapetext, (450, 700))
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:  # back to main menu
                return

        pygame.display.flip()