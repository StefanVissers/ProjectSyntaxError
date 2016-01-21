import pygame
import Menu
import time

def manual():
                         #krijgt de acties die gebeuren
    main_surface = pygame.display.set_mode((1200, 900))
    #my_font = pygame.font.SysFont("Courier", 20)
    manual_page1 = pygame.image.load('Pics/manual_page1.png')
    manual_page1 = pygame.transform.scale(manual_page1, (550, 900))
    manual_page2 = pygame.image.load('Pics/manual_page2.png')
    manual_page2 = pygame.transform.smoothscale(manual_page2, (550, 900))
    page = 0
    some_color = (255, 0, 0)
    nextpage = pygame.Rect(1150, 350, 50, 50)

    while True:
        ev = pygame.event.poll()
        mouse_pos = pygame.mouse.get_pos()
        #manualtext = my_font.render("Play Game!".format(), True, (255,255,255))
        main_surface.fill((0, 0, 128))      #Background fill first!!!!

        main_surface.blit(manual_page1, (50, 0))
        main_surface.blit(manual_page2, (600, 0))

        #nextpage = pygame.rect(x, y, breedte, hoogte)
        #lastpage = pygame.Rect()

        ev = pygame.event.poll()
        main_surface.fill(some_color, nextpage)

        if ev.type == pygame.QUIT:    #als je op de quit game knop drukt
            pygame.quit()
            quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN and nextpage.collidepoint(mouse_pos):
            print ("Werkt")
        elif ev.type == pygame.KEYDOWN:
            if ev.type == pygame.K_ESCAPE:
                Menu.menu(main_surface)

        pygame.display.flip()