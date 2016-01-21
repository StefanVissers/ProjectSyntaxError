__author__ = 'Jamal'
import pygame
class colors:
    def __init__(self, int1, int2, int3):
        self.color = ( int1, int2 , int3)


Aqua = colors(  0, 255, 255)
Black = colors(  0,   0,   0)
Blue = colors(  0,   0, 255)
Fuchsia = colors(255,   0, 255)
Gray = colors(128, 128, 128)
Green = colors(  0, 128,   0)
Lime = colors(  0, 255,   0)
Maroon = colors(128,   0,   0)
Navy_Blue = colors(  0,   0, 128)
Olive = colors(128, 128,   0)
Purple = colors(128,   0, 128)
Red = colors(255,   0,   0)
Silver = colors(192, 192, 192)
Teal = colors(  0, 128, 128)
White = colors(255, 255, 255)
Yellow = colors(255, 255,   0)

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((800, 600))
    my_font = pygame.font.SysFont("Courier", 20)
    pygame.display.set_caption("SyntaXError")
    while True:
        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            print ("YAY")
        # Other Logic Here
        my_font = pygame.font.SysFont("Courier", 20)
        main_surface.fill((Yellow))  #Background Fill First
                                        #Draw other Things After
        main_surface.fill((255,0,0), (300, 100, 150, 90))

        the_text = my_font.render("Frequency".format(), True, (255,255,255))
        main_surface.blit(the_text, (300, 100))

        pygame.display.flip()           #Display it
    pygame.quit()
main()