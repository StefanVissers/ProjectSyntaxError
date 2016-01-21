import pygame
import Menu

def manual():
    while True:
        ev = pygame.event.poll()                 #krijgt de acties die gebeuren

        main_surface = pygame.display.set_mode((1200, 900))
        my_font = pygame.font.SysFont("Courier", 20)
        #manualtext = my_font.render("Play Game!".format(), True, (255,255,255))

        main_surface.fill((0, 0, 128))      #Background fill first!!!!

        ev = pygame.event.poll()
        mouse_pos = pygame.mouse.get_pos()

        # Other stuff after!
        manual_page1 = pygame.image.load('Pics/manual_page1.png')
        manual_page1 = pygame.transform.scale(manual_page1, (550, 900))
        manual_page2 = pygame.image.load('Pics/manual_page2.png')
        manual_page2 = pygame.transform.smoothscale(manual_page2, (550, 900))
        main_surface.blit(manual_page1, (50, 0))
        main_surface.blit(manual_page2, (600, 0))

        #nextpage = pygame.rect(x, y, breedte, hoogte)
        nextpage = pygame.Rect(1100, 450, 100, 100)

        if ev.type == pygame.QUIT:    #als je op de quit game knop drukt
            pygame.quit()
            quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN and nextpage.collidepoint(mouse_pos):
            print ("Werkt")

        pygame.display.flip()