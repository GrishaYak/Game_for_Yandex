import pygame
import sys
from constants import *
from helpfull_functions import *
from global_vars import difficult
from Player import Player

screen = pygame.display.set_mode(SCREEN_SIZE)
player = Player()


def finish_the_game():
    font = pygame.font.Font(None, GAME_OVER_SIZE)
    line = font.render(GAME_OVER, True, GAME_OVER_COLOR)
    rect = pygame.Rect((SCREEN_SIZE.x - line.get_width()) // 2,
                       (SCREEN_SIZE.y - line.get_height()) // 2, *line.get_size())
    screen.blit(line, rect)


def build():
    screen.fill(MAIN_BACKGROUND_COLOR)
    pygame.display.flip()


def main():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key in KEYBINDS:
                    action = KEYBINDS[event.key]
                    IS_PRESSED[action] = True
            if event.type == pygame.KEYUP:
                if event.key in KEYBINDS:
                    IS_PRESSED[KEYBINDS[event.key]] = False
        if not player.update(*events):
            finish_the_game()
        screen.fill(MAIN_BACKGROUND_COLOR)
        screen.blit(player.image, (player.rect.x, player.rect.y))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
