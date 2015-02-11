# v0.0.2
# author Konrad Schultz
import pygame
import TetrisPieces
from pygame.locals import *


def main():
    # screen surface
    pygame.init()
    size = 920, 640
    screen = pygame.display.set_mode(size)
    # fps counter/speed regulator
    clock = pygame.time.Clock()
    # music
    pygame.mixer.music.load("sound/theme2.mp3")
    pygame.mixer.music.play(10)
    pygame.mixer.music.set_volume(0)
    # board
    board = pygame.image.load("img/board.png")
    board_rect = board.get_rect()
    t_game = TetrisPieces.TetrisApp()
    pygame.key.set_repeat(200, 50)
    loop_counter = 0
    # control loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    t_game.active.move_left(t_game)
                if event.key == K_RIGHT:
                    t_game.active.move_right(t_game)
                if event.key == K_DOWN:
                    t_game.active.move_down(t_game)
                if event.key == K_SPACE:
                    t_game.active.drop_down(t_game)
                if event.key == K_UP:
                    t_game.active.rotate_cw()  # rotate cw
                if event.key == K_v:
                    t_game.active.rotate_ccw()
        # if loop_counter % 60 == 0:
        #    t_game.active.move_down(t_game)
        #    loop_counter %= 60
        screen.blit(board, board_rect)
        t_game.active.draw(screen)
        t_game.passive.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        loop_counter += 1

if __name__ == "__main__":
    main()