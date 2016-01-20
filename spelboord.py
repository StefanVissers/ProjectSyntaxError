__author__ = 'jacob'
import pygame

bordload = pygame.image.load('Spelbord_zonderzijkanten.png')

def draw_board(the_board):

    pygame.init()
    colors = [(255,0,0), (0,0,0)]    # Set up colors [red, black]

    n = the_board       # This is an NxN chess board.
    surface_szX = 1200  # Proposed physical surface size.
    surface_szY = 850
    sq_sz = 900 // n    # sq_sz is length of a square.
    #surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_szX, surface_szY))
    surface.blit(bordload, (0, 0))
    anotherSurface = surface.convert_alpha()



    # Draw a fresh background (a blank chess board)
    for row in range(n):           # Draw each row of the board.
        c_indx = row % 2           # Change starting color on each row
        for col in range(n):       # Run through cols drawing squares
            the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
            surface.fill(colors[c_indx], the_square)
            # now flip the color index for the next square
            c_indx = (c_indx + 1) % 2




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
        main_surface.fill((0, 0, 128))  #Background Fill First
                                        #Draw other Things After
        main_surface.fill((255,0,0), (300, 100, 150, 90))

        the_text = my_font.render("Frequency".format(), True, (255,255,255))
        main_surface.blit(the_text, (300, 100))
        draw_board(18)
        pygame.display.flip()           #Display it
    pygame.quit()
main()