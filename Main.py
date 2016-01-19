__author__ = 'Stefan'
import pygame
import time



def main():
    pygame.init()
    main_surface = pygame.display.set_mode((480, 240))
    my_font = pygame.font.SysFont("Courier", 20)

    while True:
        main_surface.fill((0, 255, 0))
        pygame.display.flip()
    pygame.quit()
main()
