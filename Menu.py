__author__ = 'stefan'
import pygame
import time
import random
def menu(main_surface):
    while True:
        button = pygame.image.load('Pics/button.png').convert_alpha()
        startgamebutton = pygame.Rect(300, 100, 150, 25)
        quitgamebutton = pygame.Rect(300, 250, 150, 25)
        my_font = pygame.font.SysFont("Courier", 20)
        ev = pygame.event.poll()            #kan alle events zijn zoals mouse_click
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        if ev.type == pygame.QUIT:   # Window close button clicked?
            pygame.quit()
            quit()                   # Leave game loop
        elif ev.type == pygame.MOUSEBUTTONDOWN and startgamebutton.collidepoint(mouse_pos):   #als je op het bovenste vierkantje klikt
            print ("YAY")               #hier mmoet play game komen!
        elif ev.type == pygame.MOUSEBUTTONDOWN and quitgamebutton.collidepoint(mouse_pos):
            pygame.quit()
            quit()

        # Other Logic Here
        main_surface.fill((0, 0, 128))  #Background Fill First
                                        #Draw other Things After
        main_surface.fill((255,0,0), (300, 100, 150, 25))
        main_surface.fill((255,0,0), (300, 250, 150, 25))

        startgamebuttontext = my_font.render("Play Game!".format(), True, (255,255,255))    #geeft tekst
        quitgamebuttontext = my_font.render("Quit Game!".format(), True, (255, 255, 255))
        main_surface.blit(startgamebuttontext, (300, 100))                                 #print de tekst op het scherm
        main_surface.blit(quitgamebuttontext, (300, 250))