__author__ = 'Stefan'
import pygame
import time
import Menu
#convert_alpha voor png met transparantie! Checkt per pixel.

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("SyntaXError")

    pygame.mixer.music.load('Pics\Battle.mp3')
    pygame.mixer.music.play(-1, 0.0)

    while True:
        Menu.menu(main_surface)
        pygame.display.flip()           #Display it
main()