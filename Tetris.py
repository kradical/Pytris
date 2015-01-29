# v0.0.2
# author Konrad Schultz

import pygame
from pygame.locals import *


def pause_menu():
    pausemenu = pygame.image.load("img/pausemenu.png")
    pausemenurect = pausemenu.get_rect()
    screen.blit(pausemenu, pausemenurect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            elif event.type == KEYDOWN and event.key == K_q:
                exit()
        clock.tick(40)
        pygame.display.set_caption("fps: "+str(clock.get_fps()))

pygame.init()
size = width, height = 1045, 740
screen = pygame.display.set_mode(size)
background = pygame.image.load("img/Board.png")
backgroundrect = background.get_rect()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_q):
            pause_menu()

        screen.blit(background, backgroundrect)
        pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("fps: "+str(clock.get_fps()))