import pygame


def manual():
    main_surface = pygame.display.set_mode((1200, 850))
    my_font = pygame.font.SysFont("Courier", 20)
    manualtext = my_font.render("Play Game!".format(), True, (255,255,255))
    main_surface.blit(manualtext, (300, 100))