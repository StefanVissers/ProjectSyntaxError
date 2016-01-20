__author__ = 'stefan'
import pygame
import time
import random
import Spelbord
def menu(main_surface):
    while True:
        #startgamebuttonpng = pygame.image.load('Pics/startgame_button.png').convert_alpha()         #laad de plaatjes voor het menu
        #quitgamebuttonpng = pygame.image.load('Pics/exitgame_button.png').convert_alpha()
        #optionbuttonpng = pygame.image.load('Pics/options_button.png').convert_alpha()
        #manualgamebuttonpng = pygame.image.load('Pics/manual_button.png').convert_alpha()


        startgamebutton = pygame.Rect(150, 100, 300, 75)
        quitgamebutton = pygame.Rect(150, 250, 300, 75)
        optionbutton = pygame.Rect(150, 400, 300, 75)
        instructionbutton = pygame.Rect(150, 550, 300, 75)

        my_font = pygame.font.SysFont("Courier", 20)

        ev = pygame.event.poll()            #kan alle events zijn zoals mouse_click
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor

        if ev.type == pygame.MOUSEBUTTONDOWN and startgamebutton.collidepoint(mouse_pos):   #als je op de start game knop drukt
            Spelbord.draw_board(16)               #hier mmoet play game komen!
        elif ev.type == pygame.MOUSEBUTTONDOWN and quitgamebutton.collidepoint(mouse_pos) or ev.type == pygame.QUIT:    #als je op de quit game knop drukt
            pygame.quit()
            quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN and optionbutton.collidepoint(mouse_pos):    #als je op de opties knop drukt
            print ("OPTIES HIER")
        elif ev.type == pygame.MOUSEBUTTONDOWN and instructionbutton.collidepoint(mouse_pos):   #als je op de instructies knop drukt
            print ("INSTRUCTIES HIER")

        # Other Logic Here
        main_surface.fill((0, 0, 128))  #Background Fill First
                                        #Draw other Things After

        # main_surface.fill((255,0,0), (300, 100, 150, 25))
        # main_surface.fill((255,0,0), (300, 250, 150, 25))
        # main_surface.fill((255,0,0), (300, 400, 150, 25))
        # main_surface.fill((255,0,0), (300, 550, 150, 25))

        # startgamebuttontext = my_font.render("Play Game!".format(), True, (255,255,255))    #geeft tekst
        # quitgamebuttontext = my_font.render("Quit Game!".format(), True, (255, 255, 255))
        # optionbuttontext = my_font.render("Options!".format(), True, (255, 255, 255))
        # instructionbuttontext = my_font.render("Instructions!".format(), True, (255, 255, 255))

        # main_surface.blit(startgamebuttontext, (300, 100))                                 #print de tekst op het scherm
        # main_surface.blit(quitgamebuttontext, (300, 250))
        # main_surface.blit(optionbuttontext, (300, 400))
        # main_surface.blit(instructionbuttontext, (300, 550))

        #main_surface.blit(startgamebuttonpng, (100, 100))                                               #laat de plaatjes zien
        #main_surface.blit(quitgamebuttonpng, (100, 250))
        #main_surface.blit(optionbuttonpng, (100, 400))
        #main_surface.blit(manualgamebuttonpng, (100, 550))



        pygame.display.flip()