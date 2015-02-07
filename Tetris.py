# v0.0.2
# author Konrad Schultz

import pygame
from pygame.locals import *
import random


class Blocks(pygame.sprite.Group):
    def __init__(self, tetranimo=None):
        pygame.sprite.Group.__init__(self)
        if tetranimo is not None:
            if tetranimo == 'I':
                for x in range(4):
                    self.add(Block(tetranimo, 420+20*x, 60))
            if tetranimo == 'O':
                for x in range(2):
                    self.add(Block(tetranimo, 440+20*x, 60))
                    self.add(Block(tetranimo, 440+20*x, 80))
            if tetranimo == 'T':
                self.add(Block(tetranimo, 440, 60))
                for x in range(3):
                    self.add(Block(tetranimo, 420+20*x, 80))
            if tetranimo == 'S':
                for x in range(2):
                        self.add(Block(tetranimo, 440+20*x, 60))
                        self.add(Block(tetranimo, 420+20*x, 80))
            if tetranimo == 'Z':
                for x in range(2):
                    self.add(Block(tetranimo, 420+20*x, 60))
                    self.add(Block(tetranimo, 440+20*x, 80))
            if tetranimo == 'J':
                self.add(Block(tetranimo, 420, 60))
                for x in range(3):
                    self.add(Block(tetranimo, 420+20*x, 80))
            if tetranimo == 'L':
                self.add(Block(tetranimo, 460, 60))
                for x in range(3):
                    self.add(Block(tetranimo, 420+20*x, 80))

    def check_for_point(self):
        check_row = PlayingField(360, 480, 200, 20)
        num_collisions = len(pygame.sprite.spritecollide(check_row, self, False))

# TODO

    def move_left(self, passive, play_field):
        collide = False
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(-20, 0)
            if not pygame.sprite.collide_rect(sprite, play_field):
                collide = True
            elif pygame.sprite.groupcollide(self, passive, False, False):
                collide = True
        if collide:
            for sprite2 in iter(self):
                sprite2.rect = sprite2.rect.move(20, 0)

    def move_right(self, passive, play_field):
        collide = False
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(20, 0)
            if not pygame.sprite.collide_rect(sprite, play_field):
                collide = True
            elif pygame.sprite.groupcollide(self, passive, False, False):
                collide = True
        if collide:
            for sprite2 in iter(self):
                sprite2.rect = sprite2.rect.move(-20, 0)

    def move_down(self, block_list, passive, play_field):
        collide = False
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(0, 5)
            if not pygame.sprite.collide_rect(sprite, play_field):
                collide = True
            elif pygame.sprite.groupcollide(self, passive, False, False):
                collide = True
        if collide:
            top_row = PlayingField(360, 80, 200, 20)
            for sprite2 in iter(self):
                sprite2.rect = sprite2.rect.move(0, -5)
                self.remove(sprite2)
                passive.add(sprite2)
                if pygame.sprite.collide_rect(sprite2, top_row):
                    global dead
                    dead = True
            if not block_list:
                block_list = sequence_generator()
            if not bool(self):
                self.add(Blocks(block_list.pop()))
            passive.check_for_point()
        return collide

    def move_all_down(self, block_list, passive, play_field):
        while not self.move_down(block_list, passive, play_field):
            continue


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, xpos=None, ypos=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/"+colour+"block.png")
        self.rect = self.image.get_rect()
        if xpos is not None:
            if ypos is not None:
                self.rect = self.rect.move(xpos, ypos)


# Makes a sprite of the rectangle that would be passed into pygame.Rect
class PlayingField(pygame.sprite.Sprite):
    def __init__(self, left, top, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(left, top, w, h)


def pause_menu(screen1):
    pygame.mixer.music.set_volume(0.15)
    pausemenu = pygame.image.load("img/pausemenu.png")
    pausemenurect = pausemenu.get_rect()
    screen1.blit(pausemenu, pausemenurect)
    pygame.display.flip()
    while True:
        for event1 in pygame.event.get():
            if event1.type == QUIT:
                exit()
            if event1.type == KEYDOWN and event1.key == K_SPACE:
                return
            elif event1.type == KEYDOWN and event1.key == K_q:
                exit()


def sequence_generator():
    random_blocks = ['I', 'O', 'J', 'Z', 'S', 'T', 'L']
    random.shuffle(random_blocks)
    return random_blocks

# global game state, game over or not
dead = False


def main():
    # screen surface
    pygame.init()
    size = 920, 640
    screen = pygame.display.set_mode(size)
    # fps counter
    clock = pygame.time.Clock()
    # music
    pygame.mixer.music.load("sound/theme2.mp3")
    pygame.mixer.music.play(10)
    pygame.mixer.music.set_volume(0)
    # board
    board = pygame.image.load("img/board.png")
    board_rect = board.get_rect()
    play_field = PlayingField(360, 0, 200, 485)

    passive = Blocks()
    block_list = sequence_generator()
    active = Blocks(block_list.pop())
    counter = 0
    while not dead:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN and (event.key == K_q):
                pause_menu(screen)
                pygame.mixer.music.set_volume(0.5)
            if event.type == KEYDOWN and (event.key == K_LEFT):
                active.move_left(passive, play_field)
            if event.type == KEYDOWN and (event.key == K_RIGHT):
                active.move_right(passive, play_field)
            if event.type == KEYDOWN and (event.key == K_DOWN):
                active.move_down(block_list, passive, play_field)
            if event.type == KEYDOWN and (event.key == K_SPACE):
                active.move_all_down(block_list, passive, play_field)

        counter += 1
        clock.tick(60)
        if counter % 30 == 0:
            active.move_down(block_list, passive, play_field)
        screen.blit(board, board_rect)
        active.draw(screen)
        passive.draw(screen)
        pygame.display.flip()
    while dead:
        print("LELELELE YOU DED")

if __name__ == "__main__":
    main()




























