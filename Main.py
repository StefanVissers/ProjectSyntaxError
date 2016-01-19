__author__ = 'Stefan'
import pygame
import time



def main():
    pygame.init()
    main_surface = pygame.display.set_mode((800, 600))
    my_font = pygame.font.SysFont("Courier", 20)

    while True:
        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop
        # Other Logic Here
        my_font = pygame.font.SysFont("Courier", 20)
        main_surface.fill((0, 0, 128))  #Background Fill First
                                        #Draw other Things After
        main_surface.fill((255,0,0), (300, 100, 150, 90))

        the_text = my_font.render("Frequency"
                  .format(), True, (255,255,255))
        main_surface.blit(the_text, (300, 100))

        pygame.display.flip()           #Display it
    pygame.quit()
main()
