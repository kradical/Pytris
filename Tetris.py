import sys
import pygame


def pause_menu():
    pausemenu = pygame.image.load("img/pausemenu.png")
    screen.blit()
    while True:

    return



pygame.init()
size = width, height = 1045, 740
speed = [2, 2]
white = 255, 255, 255
screen = pygame.display.set_mode(size)
background = pygame.image.load("img/Board.png")
ball = pygame.image.load("cat.png")
ballrect = ball.get_rect()
backgroundrect = background.get_rect()

while True:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[pygame.K_q] or pygame.key.get_pressed()[pygame.K_SPACE]:
            pause_menu()
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        screen.blit(ball, ballrect)
        pygame.display.flip()
