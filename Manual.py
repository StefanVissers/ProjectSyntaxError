import Menu
import pygame


def manual():
    main_surface = pygame.display.set_mode((1200, 900))

    manual_page1 = pygame.image.load('Pics/manual/manual_page1.png')
    manual_page1 = pygame.transform.scale(manual_page1, (550, 900))
    manual_page2 = pygame.image.load('Pics/manual/manual_page2.png')
    manual_page2 = pygame.transform.smoothscale(manual_page2, (550, 900))
    manual_page3 = pygame.image.load('Pics/manual/manual_page3.png')
    manual_page3 = pygame.transform.smoothscale(manual_page3, (550, 900))
    manual_page4 = pygame.image.load('Pics/manual/manual_page4.png')
    manual_page4 = pygame.transform.smoothscale(manual_page4, (550, 900))
    manual_page5 = pygame.image.load('Pics/manual/manual_page5.png')
    manual_page5 = pygame.transform.smoothscale(manual_page5, (550, 900))
    manual_page6 = pygame.image.load('Pics/manual/manual_page6.png')
    manual_page6 = pygame.transform.smoothscale(manual_page6, (550, 900))
    manual_page7 = pygame.image.load('Pics/manual/manual_page7.png')
    manual_page7 = pygame.transform.smoothscale(manual_page7, (550, 900))
    manual_page8 = pygame.image.load('Pics/manual/manual_page8.png')
    manual_page8 = pygame.transform.smoothscale(manual_page8, (550, 900))
    manual_page9 = pygame.image.load('Pics/manual/manual_page9.png')
    manual_page9 = pygame.transform.smoothscale(manual_page9, (550, 900))
    manual_page10 = pygame.image.load('Pics/manual/manual_page10.png')
    manual_page10 = pygame.transform.smoothscale(manual_page10, (550, 900))
    manual_page11 = pygame.image.load('Pics/manual/manual_page11.png')
    manual_page11 = pygame.transform.smoothscale(manual_page11, (550, 900))
    manual_page12 = pygame.image.load('Pics/manual/manual_page12.png')
    manual_page12 = pygame.transform.smoothscale(manual_page12, (550, 900))

    some_color = (255, 0, 0)

    nextpage = pygame.image.load('Pics/next_button.png')
    previouspage = pygame.image.load('Pics/previous_button.png')
    nextpagebutton = pygame.Rect(1150, 450, 50, 50)
    previouspagebutton = pygame.Rect(0, 450, 50, 50)
    page = 0

    while True:

        main_surface.fill((0, 0, 128))      #Background fill first!!!!
        
        mouse_pos = pygame.mouse.get_pos()
        event = pygame.event.get()
        main_surface.blit(nextpage, (1150, 450))
        main_surface.blit(previouspage, (0, 450))

        for ev in event:
            if ev.type == pygame.QUIT:    #als je op de quit game knop drukt
                pygame.quit()
                quit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return
            elif ev.type == pygame.MOUSEBUTTONDOWN and nextpagebutton.collidepoint(mouse_pos):
               page += 1
            elif ev.type == pygame.MOUSEBUTTONDOWN and previouspagebutton.collidepoint(mouse_pos):
                page -= 1

        if page == 0:
            main_surface.blit(manual_page1, (50, 0))
            main_surface.blit(manual_page2, (600, 0))
        elif page == 1:
            main_surface.blit(manual_page3, (50, 0))
            main_surface.blit(manual_page4, (600, 0))
        elif page == 2:
            main_surface.blit(manual_page5, (50, 0))
            main_surface.blit(manual_page6, (600, 0))
        elif page == 3:
            main_surface.blit(manual_page7, (50, 0))
            main_surface.blit(manual_page8, (600, 0))
        elif page == 4:
            main_surface.blit(manual_page9, (50, 0))
            main_surface.blit(manual_page10, (600, 0))
        elif page == 5:
            main_surface.blit(manual_page11, (50,0))
            main_surface.blit(manual_page12, (600, 0))
        elif page > 5:
            page = 0
        elif page < 0:
            page = 5

        pygame.display.flip()