# v0.0.2
# author Konrad Schultz

import pygame
from pygame.locals import *


class Active(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)


class Block(pygame.sprite.Sprite):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("img/"+colour.upper()+"block.png")
        self.rect = self.image.get_rect()


def pause_menu():
    pygame.mixer.music.set_volume(0.15)
    pausemenu = pygame.image.load("img/pausemenu.png")
    pausemenurect = pausemenu.get_rect()
    screen.blit(pausemenu, pausemenurect)
    pygame.display.flip()
    while True:
        for event1 in pygame.event.get():
            if event1.type == QUIT:
                exit()
            if event1.type == KEYDOWN and event1.key == K_SPACE:
                return
            elif event1.type == KEYDOWN and event1.key == K_q:
                exit()
        clock.tick(40)
        pygame.display.set_caption("fps: "+str(clock.get_fps()))


def draw_screen():
    screen.blit(background, backgroundrect)

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
background = pygame.image.load("img/Board.png")
backgroundrect = background.get_rect()
clock = pygame.time.Clock()
pygame.mixer.music.load("sound/theme2.mp3")
pygame.mixer.music.play(10)
pygame.mixer.music.set_volume(0.5)

Orange = Block("O")
active = Active()
active.add(Orange)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_q):
            pause_menu()
            pygame.mixer.music.set_volume(0.5)
        draw_screen()
        active.draw(screen)
        pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("fps: "+str(clock.get_fps()))