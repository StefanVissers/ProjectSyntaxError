__author__ = 'stefan'
import pygame
import time
import random
import Spelbord
import Manual

def menu(main_surface):
    while True:
        startgamebuttonpng = pygame.image.load('Pics/startgame_button.png').convert_alpha()         #laad de plaatjes voor het menu
        manualgamebuttonpng = pygame.image.load('Pics/manual_button.png').convert_alpha()
        optionbuttonpng = pygame.image.load('Pics/options_button.png').convert_alpha()
        quitgamebuttonpng = pygame.image.load('Pics/exitgame_button.png').convert_alpha()
        background = pygame.image.load('Pics/Background.jpg').convert_alpha()

        startgamebutton = pygame.Rect(150, 100, 265, 125)
        instructionbutton = pygame.Rect(150, 250, 265, 125)
        optionbutton = pygame.Rect(150, 400, 265, 125)
        quitgamebutton = pygame.Rect(150, 550, 265, 125)

        my_font = pygame.font.SysFont("Courier", 20)

        event = pygame.event.get()            #kan alle events zijn zoals mouse_click
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN and startgamebutton.collidepoint(mouse_pos):   #als je op de start game knop drukt
                Spelbord.draw_board()               #hier mmoet play game komen!
            elif ev.type == pygame.MOUSEBUTTONDOWN and quitgamebutton.collidepoint(mouse_pos) or ev.type == pygame.QUIT:    #als je op de quit game knop drukt
                pygame.quit()
                quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and optionbutton.collidepoint(mouse_pos):    #als je op de opties knop drukt
                print ("OPTIES HIER") #TODO OPTIE MENU
            elif ev.type == pygame.MOUSEBUTTONDOWN and instructionbutton.collidepoint(mouse_pos):   #als je op de instructies knop drukt
                Manual.manual()
        # Other Logic Here
        #Background Fill First
        main_surface.blit(background, (0, 0))
        #Draw other Things After

        main_surface.blit(startgamebuttonpng, (100, 100))   #laat de plaatjes zien
        main_surface.blit(manualgamebuttonpng, (100, 250))
        main_surface.blit(optionbuttonpng, (100, 400))
        main_surface.blit(quitgamebuttonpng, (100, 550))

        pygame.display.flip()