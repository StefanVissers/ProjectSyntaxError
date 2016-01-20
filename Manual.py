import pygame

def manual():
    while True:
        ev = pygame.event.poll()                 #krijgt de acties die gebeuren
        if ev.type == ev.type == pygame.QUIT:    #als je op de quit game knop drukt
            pygame.quit()
            quit()

        main_surface = pygame.display.set_mode((1200, 900))
        my_font = pygame.font.SysFont("Courier", 20)
        manualtext = my_font.render("Play Game!".format(), True, (255,255,255))

        main_surface.fill((0, 0, 128))      #Background fill first!!!!

        # Other stuff after!

        main_surface.blit(manualtext, (300, 100))

        pygame.display.flip()