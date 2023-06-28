import pygame

def draw_box(DISPLAY, c1, c2, c3, c4, c5, c6, c7, c8):
        c1rgb = c1,c1,c1
        c2rgb = c2,c2,c2
        c3rgb = c3,c3,c3
        c4rgb = c4,c4,c4
        c5rgb = c5,c5,c5
        c6rgb = c6,c6,c6
        c7rgb = c7,c7,c7
        c8rgb = c8,c8,c8

        pygame.display.update()
        pygame.draw.rect(DISPLAY,c1rgb,(10,10,60,80))
        pygame.draw.rect(DISPLAY,c2rgb,(80,10,60,80))
        pygame.draw.rect(DISPLAY,c3rgb,(150,10,60,80))
        pygame.draw.rect(DISPLAY,c4rgb,(220,10,60,80))
        pygame.draw.rect(DISPLAY,c5rgb,(290,10,60,80))
        pygame.draw.rect(DISPLAY,c6rgb,(360,10,60,80))
        pygame.draw.rect(DISPLAY,c7rgb,(430,10,60,80))
        pygame.draw.rect(DISPLAY,c8rgb,(500,10,60,80))


def draw_text(DISPLAY, ready, c1l, c2l, c3l, c4l, c5l, c6l, c7l, c8l, pos):
        white = 255,255,255
        BLACK=(30,30,50)
        font = pygame.font.SysFont("Arial", 30)
        font2 = pygame.font.SysFont("Arial", 15)
        if ready ==True:
            text = font.render("                   position:  " + str(pos) + "                    ", True, white,BLACK)
        else:
            text = font.render("calibration is still in progress ...", True, white,BLACK)

        textRect = text.get_rect()
        textRect.center = (285 , 130 )

        text2 = font2.render("  " + str(c1l) + "  ", True, white,BLACK)
        textRect2 = text2.get_rect()
        textRect2.center = (40 ,100 )

        text3 = font2.render("  " + str(c2l) + "  ", True, white,BLACK)
        textRect3 = text3.get_rect()
        textRect3.center = (110 ,100 )

        text4 = font2.render("  " + str(c3l) + "  ", True, white,BLACK)
        textRect4 = text4.get_rect()
        textRect4.center = (180 ,100 )

        text5 = font2.render("  " + str(c4l) + "  ", True, white,BLACK)
        textRect5 = text5.get_rect()
        textRect5.center = (250 ,100 )

        text6 = font2.render("  " + str(c5l) + "  ", True, white,BLACK)
        textRect6 = text6.get_rect()
        textRect6.center = (320 ,100 )

        text7 = font2.render("  " + str(c6l) + "  ", True, white,BLACK)
        textRect7 = text7.get_rect()
        textRect7.center = (390 ,100 )

        text8 = font2.render("  " + str(c7l) + "  ", True, white,BLACK)
        textRect8 = text8.get_rect()
        textRect8.center = (460 ,100 )

        text9 = font2.render("  " + str(c8l) + "  ", True, white,BLACK)
        textRect9 = text9.get_rect()
        textRect9.center = (530 ,100 )

        DISPLAY.blit(text,textRect)
        DISPLAY.blit(text2,textRect2)
        DISPLAY.blit(text3,textRect3)
        DISPLAY.blit(text4,textRect4)
        DISPLAY.blit(text5,textRect5)
        DISPLAY.blit(text6,textRect6)
        DISPLAY.blit(text7,textRect7)
        DISPLAY.blit(text8,textRect8)
        DISPLAY.blit(text9,textRect9)
        DISPLAY.blit(text9,textRect9)
