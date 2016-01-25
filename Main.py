__author__ = 'Stefan'
import pygame
import time
import Menu
#convert_alpha voor png met transparantie! Checkt per pixel.

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0,)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

def thing_dodged(count):
    font = pygame.font.SysFont(none, 25)
    text = font.render("Dodged: " +str(count), True, BLACK)
    main_surface.blit(text, (0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def game_intro(main_surface):
    time = 0
    while True:
        main_surface.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Frequency", largeText)
        TextRect.center = ((1200/2),(900/2))
        main_surface.blit(TextSurf, TextRect)
        pygame.display.update()
        pygame.time.Clock().tick(30)
        if time == 30:
            return
        time += 1

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("SyntaXError")

    pygame.mixer.music.load('Pics\Battle.mp3')
    pygame.mixer.music.play(-1, 0.0)

    while True:
        game_intro(main_surface)
        Menu.menu(main_surface)
        pygame.display.flip()

main()
