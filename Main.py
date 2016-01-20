__author__ = 'Stefan'
import pygame
import time
import Menu
#convert_alpha voor png met transparantie! Checkt per pixel.

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((1200, 850))
    pygame.display.set_caption("SyntaXError")

    #pygame.mixer.init()
    #pygame.mixer.pre_init(44100, 16, 2, 4096)
    #soundObj = pygame.mixer.Sound('meep_merp.mp3')
    #soundObj.play()
    #import time
    #time.sleep(1) # wait and let the sound play for 1 second
    #soundObj.stop()
    #pygame.mixer.music.load('content\meep_merp.mp3')
    #pygame.mixer.music.play(-5, 0.0)
    while True:
        Menu.menu(main_surface)
        pygame.display.flip()           #Display it
main()