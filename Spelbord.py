from Tile import *
from UnitClasses import *
import Menu

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
quitingamebutton = pygame.Rect(900, 0, 265, 125)
shop = pygame.Rect(950, 200, 200, 50)
ViewSoldierButton = pygame.Rect(900, 700, 500, 50)
ViewTankButton = pygame.Rect(900, 750, 500, 50)
ViewRobotButton = pygame.Rect(900, 800, 500, 50)
ViewBoatButton = pygame.Rect(900, 850, 500, 50)
shopmenubutton = pygame.image.load('Pics/units/shop_menu_button.png')


def reload(Map):                                                       # herinstantieert het bord
    main_surface.blit(background, (0,0))
    main_surface.blit(quit_in_gamebuttonpng, (900, 0))
    main_surface.blit(bordload, (0,0))
    main_surface.blit(shopmenubutton, (950, 200))
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

        if coordinates is not None:
              soldierCounttext = font.render(str(countSoldiers(coordinates, Map)), 1, (255,255,0))
              main_surface.fill((0, 0 , 0), (ViewSoldierButton))
              main_surface.blit(soldierCounttext, (900, 700))
              tankCounttext = font.render(str(countTanks(coordinates, Map)), 1, (255,0,0))
              main_surface.fill((0, 0 , 0), (ViewTankButton))
              main_surface.blit(tankCounttext, (900, 750))
              robotCounttext = font.render(str(countRobots(coordinates, Map)), 1, (255,50,0))
              main_surface.fill((0, 0 , 0), (ViewRobotButton))
              main_surface.blit(robotCounttext, (900, 800))
              boatCounttext = font.render(str(countBoats(coordinates, Map)), 1, (255,100,0))
              main_surface.fill((0, 0 , 0), (ViewBoatButton))
              main_surface.blit(boatCounttext, (900, 850))


        countUnits(coordinates, Map)
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

        if soldier == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            unit = UnitClasses.Soldier(None)
                            i.Soldier.append(unit)
                            soldier = 0

        if tank == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            unit = UnitClasses.Tank(None)
                            i.Tank.append(unit)
                            tank = 0

        if robot == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        if i.Barack == True or i.Base == True:
                            unit = UnitClasses.Robot(None)
                            i.Robot.append(unit)
                            robot = 0

        if boot == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is False:
                        unit = UnitClasses.Boat(None)
                        i.Boat.append(unit)
                        boot = 0

        if barak == 1:
            if coordinates is not None:
                for i in Map:
                    if coordinates.Position.x == i.Position.x and coordinates.Position.y == i.Position.y and i.Traversable is True:
                        i.Barack = True
                        barak = 0

        if coordinates is not None and coordinates1 is None:
            if (coordinates.Soldier != [] or coordinates.Tank != [] or coordinates.Robot != [] or coordinates.Boat != []):
                coordinates1 = getTile(event, mouse_pos, Map)

        if coordinates1 != coordinates and coordinates is not None and coordinates1 is not None:
            if (coordinates1.Soldier != [] or coordinates1.Tank != [] or coordinates1.Robot != [] or coordinates1.Boat != []):
                coordinates2 = getTile(event, mouse_pos, Map)
                Tile.selectUnit(coordinates1, coordinates2, Map)
                coordinates1 = None
                coordinates2 = None
                coordinates = None
                reload(Map)
        drawUnits(Map)

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
            klik = 0

        pygame.display.flip()