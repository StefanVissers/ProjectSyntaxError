__author__ = 'Stefan/Jacob'
import pygame
import time
import Menu
#convert_alpha voor png met transparantie! Checkt per pixel.

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0,)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)


def game_intro(main_surface):
    Figuur1 = pygame.image.load('Pics/intro/1.png')
    Figuur2 = pygame.image.load('Pics/intro/2.png')
    Figuur3 = pygame.image.load('Pics/intro/3.png')
    Figuur4 = pygame.image.load('Pics/intro/4.png')
    Figuur5 = pygame.image.load('Pics/intro/5.png')
    Figuur6 = pygame.image.load('Pics/intro/6.png')
    Figuur7 = pygame.image.load('Pics/intro/7.png')
    Figuur8 = pygame.image.load('Pics/intro/8.png')
    Figuur9 = pygame.image.load('Pics/intro/9.png')
    Figuur10 = pygame.image.load('Pics/intro/10.png')
    Figuur11 = pygame.image.load('Pics/intro/11.png')
    Figuur12 = pygame.image.load('Pics/intro/12.png')
    time = 0
    while True:
        pygame.display.update()
        pygame.time.Clock().tick(10)                                    # 10 fps
        if time == 0:
            main_surface.blit(Figuur1, (0,0))
        elif time == 6:
            main_surface.blit(Figuur2, (0,0))
        elif time == 7:
            main_surface.blit(Figuur3, (0,0))
        elif time == 8:
            main_surface.blit(Figuur4, (0,0))
        elif time == 9:
            main_surface.blit(Figuur5, (0,0))
        elif time == 10:
            main_surface.blit(Figuur6, (0,0))
        elif time == 11:
            main_surface.blit(Figuur7, (0,0))
        elif time == 12:
            main_surface.blit(Figuur8, (0,0))
        elif time == 13:
            main_surface.blit(Figuur9, (0,0))
        elif time == 14:
            main_surface.blit(Figuur10, (0,0))
        elif time == 15:
            main_surface.blit(Figuur11, (0,0))
        elif time == 16:
            main_surface.blit(Figuur12, (0,0))
        elif time == 40:
            return
        time += 1


def main():
    pygame.init()
    main_surface = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("SyntaXError")

    while True:
        # game_intro(main_surface)                                      # begint de intro
        Menu.menu(main_surface)
        pygame.display.flip()

main()