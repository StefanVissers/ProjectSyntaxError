__author__ = 'stefan'
import pygame
import Spelbord
import Manual

def menu(main_surface):
    maintheme = pygame.mixer.Sound('Pics/sound/maintheme2.wav')
    muziek = 0
    while True:
        if muziek == 0:
            pygame.mixer.Sound.play(maintheme, -1)
            muziek = 1
        startgamebuttonpng = pygame.image.load('Pics/startgame_button.png').convert_alpha()         #laad de plaatjes voor het menu
        manualgamebuttonpng = pygame.image.load('Pics/manual_button.png').convert_alpha()
        quitgamebuttonpng = pygame.image.load('Pics/exitgame_button.png').convert_alpha()
        background = pygame.image.load('Pics/Background.jpg').convert_alpha()


        startgamebutton = pygame.Rect(150, 100, 265, 125)
        instructionbutton = pygame.Rect(150, 250, 265, 125)
        quitgamebutton = pygame.Rect(150, 550, 265, 125)

        event = pygame.event.get()            #kan alle events zijn zoals mouse_click
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor
        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN and startgamebutton.collidepoint(mouse_pos):   #als je op de start game knop drukt
                pygame.mixer.Sound.fadeout(maintheme, 2500)
                Spelbord.draw_board()               #hier moet play game komen!
                muziek = 0
            elif ev.type == pygame.MOUSEBUTTONDOWN and quitgamebutton.collidepoint(mouse_pos) or ev.type == pygame.QUIT:    #als je op de quit game knop drukt
                pygame.quit()
                quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and instructionbutton.collidepoint(mouse_pos):   #als je op de instructies knop drukt
                Manual.manual()

        main_surface.blit(background, (0, 0))
        #Draw other Things After

        main_surface.blit(startgamebuttonpng, (100, 100))   #laat de plaatjes zien
        main_surface.blit(manualgamebuttonpng, (100, 250))
        main_surface.blit(quitgamebuttonpng, (100, 550))

        pygame.display.flip()