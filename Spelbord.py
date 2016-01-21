__author__ = 'jacob'
import pygame
import Menu

bordload = pygame.image.load('Pics/Spelbord_zonderzijkanten.png')
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0,)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

def draw_board(the_board):
    main_surface = pygame.display.set_mode((1200, 900))
    pygame.init()
    colors = [(BLUE), (BLACK)]    # Set up colors [red, black]
    while True:
        ev = pygame.event.poll()

        n = the_board       # This is an NxN chess board.
        surface_szX = 1200  # Proposed physical surface size.
        surface_szY = 900
        sq_sz = 900 // n    # sq_sz is length of a square.
        surface_sz = n * sq_sz     # Adjust to exactly fit n squares.
    
        # Create the surface of (width, height), and its window.
        surface = pygame.display.set_mode((surface_szX, surface_szY))

    
        #Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Change starting color on each row
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        surface.blit(bordload, (0,0))
    
        if ev.type == pygame.QUIT:   # Window close button clicked?
            pygame.quit()
            quit()
        elif ev.type == pygame.K_ESCAPE:
            Menu.menu(main_surface)




        quit_in_gamebuttonpng = pygame.image.load('Pics/exit_in_game.png').convert_alpha()
        quitingamebutton = pygame.Rect(0, 0, 300, 125)
        if ev.type == pygame.MOUSEBUTTONDOWN and quitingamebutton.collidepoint(mouse_pos):
            Menu.menu()

        main_surface.blit(quit_in_gamebuttonpng, (900, 0))
        pygame.display.flip()