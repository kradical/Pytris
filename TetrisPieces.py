import pygame
import random


# global properties of the instance of the application
class TetrisApp():
    def __init__(self):
        self.block_list = [['I', 'O', 'S', 'Z', 'J', 'L', 'T'], ['I', 'O', 'S', 'Z', 'J', 'L', 'T']]
        random.shuffle(self.block_list[0])
        random.shuffle(self.block_list[1])
        self.block_in_sequence = 0
        self.passive = Blocks()
        self.active = MovingBlocks(self.block_list[0][self.block_in_sequence])
        self.play_field = PlayingField(360, 0, 200, 485)

    def new_active(self):
        self.block_in_sequence += 1
        self.block_in_sequence %= 7
        if self.block_in_sequence == 0:
            self.block_list[0], self.block_list[1] = self.block_list[1], self.block_list[0]
            random.shuffle(self.block_list[1])
        self.active = MovingBlocks(self.block_list[0][self.block_in_sequence])


# Makes a sprite of the rectangle that would be passed into pygame.Rect
# useful for sprite.collide type methods
class PlayingField(pygame.sprite.Sprite):
    def __init__(self, left, top, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(left, top, w, h)


# any group of blocks
class Blocks(pygame.sprite.Group):
    def move_down(self, t_game):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(0, 20)
        self.center[1] += 20
        if t_game is not None and self.check_for_collisions(t_game.passive, t_game.play_field):
            self.move_up()
            for sprite in iter(self):
                self.remove(sprite)
                t_game.passive.add(sprite)
            t_game.passive.check_for_point()
            t_game.new_active()
            return False
        else:
            return True

    def move_up(self):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(0, -20)

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
class MovingBlocks(Blocks):
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
            return [460, 80]
        else:
            return [440, 100]

    def move_left(self, t_game=None):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(-20, 0)
        self.center[0] -= 20
        if t_game is not None and self.check_for_collisions(t_game.passive, t_game.play_field):
            self.move_right()

    def move_right(self, t_game=None):
        for sprite in iter(self):
            sprite.rect = sprite.rect.move(20, 0)
        self.center[0] += 20
        if t_game is not None and self.check_for_collisions(t_game.passive, t_game.play_field):
            self.move_left()

    def drop_down(self, t_game):
        while self.move_down(t_game):
            pass

    def rotate_cw(self):
        if self.type == 'O':
            pass
        elif self.type == 'I':
            self.rotate_state += 1
            self.rotate_state %= 4
            for sprite in iter(self):
                self.remove(sprite)
            if self.rotate_state == 0:
                for x in range(4):
                    self.add(Block(self.type, self.center[0]-40+20*x, self.center[1]-20))
            elif self.rotate_state == 1:
                for x in range(4):
                    self.add(Block(self.type, self.center[0], self.center[1]-40+20*x))
            elif self.rotate_state == 2:
                for x in range(4):
                    self.add(Block(self.type, self.center[0]-40+20*x, self.center[1]))
            else:
                for x in range(4):
                    self.add(Block(self.type, self.center[0]-20, self.center[1]-40+20*x))
        else:
            for sprite in iter(self):
                # left
                if sprite.rect.left < self.center[0]:
                    # bot
                    if sprite.rect.top > self.center[1]:
                        sprite.rect.top -= 40
                    # mid
                    elif sprite.rect.top == self.center[1]:
                        sprite.rect.left += 20
                        sprite.rect.top -= 20
                    # top
                    else:
                        sprite.rect.left += 40
                # mid
                elif sprite.rect.left == self.center[0]:
                    # bot
                    if sprite.rect.top > self.center[1]:
                        sprite.rect.top -= 20
                        sprite.rect.left -= 20
                    # top
                    elif sprite.rect.top < self.center[1]:
                        sprite.rect.top += 20
                        sprite.rect.left += 20
                # right
                else:
                    # bot
                    if sprite.rect.top > self.center[1]:
                        sprite.rect.left -= 40
                    # mid
                    elif sprite.rect.top == self.center[1]:
                        sprite.rect.left -= 20
                        sprite.rect.top += 20
                    # top
                    else:
                        sprite.rect.top += 40

    def rotate_ccw(self):
        if self.type == 'O':
            pass
        elif self.type == 'I':
            self.rotate_state += 3
            self.rotate_state %= 4
            for sprite in iter(self):
                self.remove(sprite)
            if self.rotate_state == 0:
                for x in range(4):
                    self.add(Block(self.type, self.center[0]-40+20*x, self.center[1]-20))
            elif self.rotate_state == 1:
                for x in range(4):
                    self.add(Block(self.type, self.center[0], self.center[1]-40+20*x))
            elif self.rotate_state == 2:
                for x in range(4):
                    self.add(Block(self.type, self.center[0]-40+20*x, self.center[1]))
            else:
                for x in range(4):
                    self.add(Block(self.type, self.center[0]-20, self.center[1]-40+20*x))
        # rotate for all 3x3 bricks
        else:
            for sprite in iter(self):
                # left
                if sprite.rect.left < self.center[0]:
                    # bot
                    if sprite.rect.top > self.center[1]:
                        sprite.rect.left += 40
                    # mid
                    elif sprite.rect.top == self.center[1]:
                        sprite.rect.left += 20
                        sprite.rect.top += 20
                    # top
                    else:
                        sprite.rect.top += 40
                # mid
                elif sprite.rect.left == self.center[0]:
                    # bot
                    if sprite.rect.top > self.center[1]:
                        sprite.rect.top -= 20
                        sprite.rect.left += 20
                    # top
                    elif sprite.rect.top < self.center[1]:
                        sprite.rect.top += 20
                        sprite.rect.left -= 20
                # right
                else:
                    # bot
                    if sprite.rect.top > self.center[1]:
                        sprite.rect.top -= 40
                    # mid
                    elif sprite.rect.top == self.center[1]:
                        sprite.rect.left -= 20
                        sprite.rect.top -= 20
                    # top
                    else:
                        sprite.rect.left -= 40


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, x_offset, y_offset):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/"+colour+"block.png")
        self.rect = self.image.get_rect().move(x_offset, y_offset)