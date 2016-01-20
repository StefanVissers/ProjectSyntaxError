__author__ = 'Stefan'
import pygame
import time

#convert_alpha voor png met transparantie! Checkt per pixel.

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((800, 600))
    my_font = pygame.font.SysFont("Courier", 20)
    pygame.display.set_caption("SyntaXError")
    button = pygame.image.load('Pics/button.png').convert_alpha()
    rectangle = pygame.Rect(300, 100, 150, 25)
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    soundObj = pygame.mixer.Sound('meep_merp.mp3')
    soundObj.play()
    import time
    time.sleep(1) # wait and let the sound play for 1 second
    soundObj.stop()
    
    while True:
        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()            #kan alle events zijn zoals mouse_click
        mouse_pos = pygame.mouse.get_pos()  #krijgt de positie van de cursor

        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop
        elif ev.type == pygame.MOUSEBUTTONDOWN and rectangle.collidepoint(mouse_pos):   #als je op het bovenste vierkantje klikt
            print ("YAY")               #hier mmoet play game komen!
        # Other Logic Here
        main_surface.fill((0, 0, 128))  #Background Fill First
                                        #Draw other Things After
        main_surface.fill((255,0,0), (300, 100, 150, 25))

        the_text = my_font.render("Play Game!".format(), True, (255,255,255))    #geeft tekst
        main_surface.blit(the_text, (300, 100))                                 #print de tekst op het scherm

        pygame.display.flip()           #Display it
    pygame.quit()
main()
