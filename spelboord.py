__author__ = 'jacob'
import pygame
import Menu

bordload = pygame.image.load('Pics/Spelbord_zonderzijkanten.png')

def draw_board(the_board):
    main_surface = pygame.display.set_mode((1200, 850))
    pygame.init()
    colors = [(0,0,255), (0,0,0)]    # Set up colors [red, black]
    while True:
        ev = pygame.event.poll()
        
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
    
        if ev.type == pygame.QUIT:   # Window close button clicked?
            pygame.quit()
            quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            Menu.menu(main_surface)
        pygame.display.flip()