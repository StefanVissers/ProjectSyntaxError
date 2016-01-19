__author__ = 'Stefan'
import pygame
import time



def main():
    pygame.init()
    main_surface = pygame.display.set_mode((1920, 1080))
    my_font = pygame.font.SysFont("Courier", 20)

    while True:
        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop
        # Other Logic Here

        main_surface.fill((0, 255, 0))  #Background Fill First
                                        #Draw other Things After



        pygame.display.flip()           #Display it
    pygame.quit()
main()
