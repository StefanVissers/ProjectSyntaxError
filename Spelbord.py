from Tile import *
from UnitClasses import *
import Menu
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

quit_in_gamebuttonpng = pygame.image.load('Pics/exitgame_button.png').convert_alpha()
areyousurepng = pygame.image.load('Pics/areyousure.png').convert_alpha()
bordload = pygame.image.load('Pics/Spelbord_zonderzijkanten.png')
background = pygame.image.load('Pics/Background.jpg')
manualbutton = pygame.image.load('Pics/manual_button.png').convert_alpha()
quitingamebutton = pygame.Rect(900, 0, 265, 125)
shop = pygame.Rect(950, 200, 200, 50)
manual = pygame.Rect(900, 100, 200, 100)
ViewSoldierButton = pygame.Rect(900, 700, 500, 50)
ViewTankButton = pygame.Rect(900, 750, 500, 50)
ViewRobotButton = pygame.Rect(900, 800, 500, 50)
ViewBoatButton = pygame.Rect(900, 850, 500, 50)
shopmenubutton = pygame.image.load('Pics/units/shop_menu_button.png')
moneydisplay = pygame.Rect(1100, 450, 200, 50)
#TODO A RECTANGLE WITH MONEY VARIABLE IS DISPLAYED ABOVE THE SHOP
BaseMoney = Base(1)

def reload(Map):                                                       # herinstantieert het bord
    main_surface.blit(background, (0,0))
    main_surface.blit(quit_in_gamebuttonpng, (900, 0))
    main_surface.blit(bordload, (0,0))
    main_surface.blit(shopmenubutton, (950, 200))
    main_surface.blit(manualbutton, (900, 100))
    drawBase(Map)

def draw_board():
    main_surface.blit(background, (0,0))
    main_surface.blit(quit_in_gamebuttonpng, (900, 0))
    main_surface.blit(bordload, (0,0))

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
    main_surface.blit(shopmenubutton, (950, 200))
    coordinates1 = None
    font = pygame.font.SysFont(None, 25)

    Map = Tile.create_Tilelist()
    drawBase(Map)
    zetten = 0
    players = [Base(1), Base(2), Base(3), Base(4)]
    currentplayer = players[0].Player

    while True:
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        event = pygame.event.get()            #kan alle events zijn zoals mouse_click
        coordinates = getTile(event, mouse_pos, Map)
        drawMoney(BaseMoney.Money)

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
            elif ev.type == pygame.MOUSEBUTTONDOWN and manual.collidepoint(mouse_pos):
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

        #TODO if a unit is built money is substracted
        if soldier == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            unit = UnitClasses.Soldier(currentplayer)
                            print("De huidige player = "+ str(currentplayer))
                            i.Soldier.append(unit)
                            soldier = 0
                            zetten += 1
                            print("Het aantal zetten = " +str(zetten))

        if tank == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            unit = UnitClasses.Tank(currentplayer)
                            i.Tank.append(unit)
                            tank = 0
                            zetten += 1
                            print("Het aantal zetten = " +str(zetten))

        if robot == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            unit = UnitClasses.Robot(currentplayer)
                            i.Robot.append(unit)
                            robot = 0
                            zetten += 1
                            print("Het aantal zetten = " +str(zetten))

        #TODO a boat can only be spawned next to a unit in water
        if boot == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is False:
                        for i in Map:
                            if (coordinates.Position.x + 1 == i.Position.x and coordinates.Position.y == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    or (coordinates.Position.x - 1 == i.Position.x and coordinates.Position.y == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    or (coordinates.Position.x == i.Position.x and coordinates.Position.y + 1 == i.Position.y and (i.Robot or i.Soldier or i.Tank))\
                                    or (coordinates.Position.x == i.Position.x and coordinates.Position.y - 1 == i.Position.y and (i.Robot or i.Soldier or i.Tank)):
                                unit = UnitClasses.Boat(currentplayer)
                                coordinates.Boat.append(unit)
                                boot = 0
                                zetten += 1
                                print(zetten)

        #TODO a barack can only be spawned on a unit
        if barak == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if len(i.Soldier) >= 1 or len(i.Tank) >= 1 or len(i.Robot) >= 1:                      
                            i.Barack = True
                            barak = 0
                            zetten += 1
                            print("Het aantal zetten = " +str(zetten))


        #TODO Players can only move units when a unit their playernumber == (x)
        if coordinates is not None and coordinates1 is None:
            if (coordinates.Soldier != [] or coordinates.Tank != [] or coordinates.Robot != [] or coordinates.Boat != []):
                if len(coordinates.Soldier) > 0:
                    soldiercheck = 0
                    for i in coordinates.Soldier:
                        if i.Player == currentplayer:
                            soldiercheck += 1
                            if soldiercheck == len(coordinates.Soldier):
                                coordinates1 = getTile(event, mouse_pos, Map)
                if len(coordinates.Robot) > 0:
                    robotcheck = 0
                    for i in coordinates.Robot:
                        if i.Player == currentplayer:
                            robotcheck += 1
                            if robotcheck == len(coordinates.Robot):
                                coordinates1 = getTile(event, mouse_pos, Map)
                if len(coordinates.Tank) > 0:
                    tankcheck = 0
                    for i in coordinates.Tank:
                        if i.Player == currentplayer:
                            tankcheck += 1
                            if tankcheck == len(coordinates.Tank):
                                coordinates1 = getTile(event, mouse_pos, Map)
                if len(coordinates.Boat) > 0:
                    boatcheck = 0
                    for i in coordinates.Boat:
                        if i.Player == currentplayer:
                            boatcheck += 1
                            if boatcheck == len(coordinates.Boat):
                                coordinates1 = getTile(event, mouse_pos, Map)

        if coordinates1 != coordinates and coordinates is not None and coordinates1 is not None:
            if (coordinates1.Soldier != [] or coordinates1.Tank != [] or coordinates1.Robot != [] or coordinates1.Boat != []):
                    coordinates2 = getTile(event, mouse_pos, Map)
                    Tile.selectUnit(coordinates1, coordinates2, Map)
                    zetten += 1
                    print("Het aantal zetten = " +str(zetten))
                    coordinates1 = None
                    coordinates2 = None
                    coordinates = None
                    reload(Map)
        drawUnits(Map, currentplayer)

        #TODO Get a good picture in the middle of the screen that displays which player his turn it is
        if zetten == 4:
            print("De beurt van player " + str(currentplayer) + " is nu voorbij")
            currentplayer = turn(currentplayer)
            print("De beurt van player " + str(currentplayer) + " begint nu")
            zetten = 0
            TurnText = font.render("Current player : " + str(currentplayer), 1, (255,255,255))
            main_surface.blit(TurnText, (970, 150))

        if klik == 1:
            main_surface.blit(areyousurepng, (300, 200))
            yesbutton = pygame.Rect(410, 415, 190, 100)    # position yes button
            nobutton = pygame.Rect(630, 415, 190, 100)     # position no button
            if ev.type == pygame.MOUSEBUTTONDOWN and yesbutton.collidepoint(mouse_pos):
                Menu.menu(main_surface)
            elif ev.type == pygame.MOUSEBUTTONDOWN and nobutton.collidepoint(mouse_pos):
                klik = 2
        elif klik == 2:
            main_surface.blit(bordload, (0,0))
            reload(Map)
            klik = 0

        pygame.display.flip()