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

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)                        # text colour
    return textSurface, textSurface.get_rect()

def game_intro(main_surface):
    time = 0
    while True:
        main_surface.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf',115)            # text font
        TextSurf, TextRect = text_objects("Frequency", largeText)       # display text
        TextRect.center = ((1200/2),(900/2))                            # center the text
        main_surface.blit(TextSurf, TextRect)
        pygame.display.update()
        pygame.time.Clock().tick(30)                                    # 30 fps
        if time == 30:
            return
        time += 1

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("SyntaXError")

    # pygame.mixer.music.load('Pics/sound/Battle.mp3')
    # pygame.mixer.music.play(-1, 0.0)

    while True:
        game_intro(main_surface)                                      # begint de intro
        Menu.menu(main_surface)
        pygame.display.flip()

main()
