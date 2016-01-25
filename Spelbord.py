import pygame
import Menu
from Tile import *

bordload = pygame.image.load('Pics/Spelbord_zonderzijkanten.png')
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

    quitingamebutton = pygame.Rect(900, 0, 265, 125)
    main_surface.blit(quit_in_gamebuttonpng, (900, 0))
    main_surface.blit(bordload, (0,0))
    klik = 0
    testlist = []

    createBase()

    while True:
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        ev = pygame.event.poll()            #kan alle events zijn zoals mouse_click

        if ev.type == pygame.MOUSEBUTTONDOWN and quitingamebutton.collidepoint(mouse_pos):
            klik = 1
            # Menu.menu(main_surface)
        if klik == 1:
            main_surface.blit(areyousurepng, (300, 200))
            yes123 = pygame.Rect(410, 415, 190, 100)    # position yes button
            no123 = pygame.Rect(630, 415, 190, 100)     # position no button
            if ev.type == pygame.MOUSEBUTTONDOWN and yes123.collidepoint(mouse_pos):
                Menu.menu(main_surface)
            elif ev.type == pygame.MOUSEBUTTONDOWN and no123.collidepoint(mouse_pos):
                klik = 2
        elif klik == 2:
            main_surface.blit(bordload, (0,0))
            klik = 0

        if ev.type == pygame.QUIT:   # Window close button clicked?
            pygame.quit()
            quit()
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:   # back to main menu
            klik = 1

        pygame.display.flip()
