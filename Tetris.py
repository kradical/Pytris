# v0.0.2
# author Konrad Schultz

import pygame
from pygame.locals import *


class Blocks(pygame.sprite.Group):
    def __init__(self, tetranimo=None):
        pygame.sprite.Group.__init__(self)
        if tetranimo is not None:
            if tetranimo == 'I':
                for x in range(4):
                    cy = Block("I", 415+20*x, 80)
                    self.add(cy)
            if tetranimo == 'O':
                print("Yellow")
            if tetranimo == 'T':
                print("Purple")
            if tetranimo == 'S':
                print("Green")
            if tetranimo == 'Z':
                print("Red")
            if tetranimo == 'J':
                print("Blue")
            if tetranimo == 'L':
                print("Orange")

    def move_left(self):
        pass

    def move_right(self):
        pass


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, xpos=None, ypos=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/"+colour+"block.png")
        self.rect = self.image.get_rect()
        if xpos is not None:
            if ypos is not None:
                self.rect = self.rect.move(xpos, ypos)


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
        clock.tick(60)
        pygame.display.set_caption("fps: "+str(clock.get_fps()))


def initialize_border():
    for x in range(4, 26):
        grey = Block("g")
        grey2 = Block("g")
        grey.rect = grey.rect.move(335, 20*x)
        grey2.rect = grey2.rect.move(555, 20*x)
        Border.add(grey)
        Border.add(grey2)
    for x in range(10):
        grey = Block("g")
        grey.rect = grey.rect.move(335+20*x, 20*25)
        Border.add(grey)

# screen surface
pygame.init()
size = width, height = 950, 650
screen = pygame.display.set_mode(size)
# fps counter
clock = pygame.time.Clock()
# music
pygame.mixer.music.load("sound/theme2.mp3")
pygame.mixer.music.play(10)
pygame.mixer.music.set_volume(0.5)
# border
Border = Blocks()
initialize_border()

Active = Blocks("I")

while True:
    for event in pygame.event.get():
        screen.fill([200, 200, 100])
        Border.draw(screen)
        Active.draw(screen)
        pygame.display.flip()
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_q):
            pause_menu()
            pygame.mixer.music.set_volume(0.5)
        if event.type == KEYDOWN and (event.key == K_LEFT):
            Active.move_left()
        if event.type == KEYDOWN and (event.key == K_RIGHT):
            Active.move_right()
    clock.tick(60)
    pygame.display.set_caption("fps: "+str(clock.get_fps()))