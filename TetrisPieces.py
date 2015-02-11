import pygame
import random


class TetrisApp():
    def __init__(self):
        self.block_list = [['I', 'O', 'S', 'Z', 'J', 'L', 'T'], ['I', 'O', 'S', 'Z', 'J', 'L', 'T']]
        random.shuffle(self.block_list[0])
        random.shuffle(self.block_list[1])
        self.block_in_sequence = 0
        self.passive = Blocks()
        self.active = mBlocks(self.block_list[0][self.block_in_sequence])
        self.play_field = PlayingField(360, 0, 200, 485)


# Makes a sprite of the rectangle that would be passed into pygame.Rect
# useful for sprite.collide type methods
class PlayingField(pygame.sprite.Sprite):
    def __init__(self, left, top, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(left, top, w, h)


#any group of blocks
class Blocks(pygame.sprite.Group):
    def move_down(self, t_game):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(0, 20)
            self.center[1] += 20
        if t_game is not None and self.check_for_collisions(t_game.passive, t_game.play_field):
            self.move_up()

    def move_up(self):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(0, -20)
            self.center[1] -= 20

    def check_for_collisions(self, group_of_blocks, play_field):
        if len(pygame.sprite.spritecollide(play_field, self, False)) != 4:
            return True
        elif pygame.sprite.groupcollide(self, group_of_blocks, False, False):
            return True
        else:
            return False

    def check_for_point(self):
        rows_down = 0
        rows_removed = False
        for x in range(20):
            check_row = PlayingField(360, 480-20*x, 200, 20)
            num_collisions = pygame.sprite.spritecollide(check_row, self, False)
            if len(num_collisions) == 10:
                self.remove(num_collisions)
                rows_removed = True
                rows_down += 1
            for sprite in num_collisions:
                sprite.rect = sprite.rect.move(0, 20*rows_down)
        return rows_removed


#active 4 block unit
class mBlocks(Blocks):
    def __init__(self, tetranimo):
        pygame.sprite.Group.__init__(self)
        self.rotate_state = 0
        self.type = tetranimo
        self.center = self.initialize_center()
        if self.type == 'I':
            for x in range(4):
                self.add(Block(tetranimo, 420+20*x, 60))
        elif tetranimo == 'O':
            for x in range(2):
                self.add(Block(tetranimo, 440+20*x, 60))
                self.add(Block(tetranimo, 440+20*x, 80))
        elif tetranimo == 'T':
            self.center = [440, 80]
            self.add(Block(tetranimo, 440, 60))
            for x in range(3):
                self.add(Block(tetranimo, 420+20*x, 80))
        elif tetranimo == 'S':
            self.center = [440, 80]
            for x in range(2):
                    self.add(Block(tetranimo, 440+20*x, 60))
                    self.add(Block(tetranimo, 420+20*x, 80))
        elif tetranimo == 'Z':
            self.center = [440, 80]
            for x in range(2):
                self.add(Block(tetranimo, 420+20*x, 60))
                self.add(Block(tetranimo, 440+20*x, 80))
        elif tetranimo == 'J':
            self.center = [440, 80]
            self.add(Block(tetranimo, 420, 60))
            for x in range(3):
                self.add(Block(tetranimo, 420+20*x, 80))
        elif tetranimo == 'L':
            self.center = [440, 80]
            self.add(Block(tetranimo, 460, 60))
            for x in range(3):
                self.add(Block(tetranimo, 420+20*x, 80))

    def initialize_center(self):
        if self.type == 'I':
            return [450, 70]
        elif self.type == 'O':
            return [450, 70]
        else:
            return [440, 80]

    def move_left(self, t_game=None):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(-20, 0)
        if t_game is not None and self.check_for_collisions(t_game.passive, t_game.play_field):
            self.move_right()

    def move_right(self, t_game=None):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(20, 0)
        if t_game is not None and self.check_for_collisions(t_game.passive, t_game.play_field):
            self.move_left()

    def drop_down(self, t_game):
        self.move_down(t_game)


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, x_offset, y_offset):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/"+colour+"block.png")
        self.rect = self.image.get_rect().move(x_offset, y_offset)