import pygame
import Menu
from Tile import *
from UnitClasses import *

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0,)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
main_surface = pygame.display.set_mode((1200, 900))
offset = 50

def draw_board():
    quit_in_gamebuttonpng = pygame.image.load('Pics/exitgame_button.png').convert_alpha()
    areyousurepng = pygame.image.load('Pics/areyousure.png').convert_alpha()
    bordload = pygame.image.load('Pics/Spelbord_zonderzijkanten.png')

    quitingamebutton = pygame.Rect(900, 0, 265, 125)
    main_surface.blit(quit_in_gamebuttonpng, (900, 0))
    main_surface.blit(bordload, (0,0))
    klik = 0
    menu = 0
    testlist = []
    #drawUnits()

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
    main_surface.blit(quit_in_gamebuttonpng, (900, 0))

    army = []
    Map = Tile.create_Tilelist()
    Base1 = UnitClasses.Base(1, Map[0])
    Base1.Tile.Barack = True
    army.append(Base1)


    while True:
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        event = pygame.event.get()            #kan alle events zijn zoals mouse_click

        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN and quitingamebutton.collidepoint(mouse_pos):
                klik = 1
                # Menu.menu(main_surface)
            elif ev.type == pygame.QUIT:   # Window close button clicked?
                pygame.quit()
                quit()
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:   # back to main menu
                klik = 1
            elif ev.type == pygame.MOUSEBUTTONDOWN and shopmenuButton1.collidepoint(mouse_pos):
                print ("SPAWN UNIT")

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

        coordinates = getTile(event, mouse_pos)

        drawUnits(coordinates)



        pygame.display.flip()