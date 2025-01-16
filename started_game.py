import pygame
import sys
from constants import *
from helpfull_functions import *
import start_screen


def main(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key in KEYBINDS:
                    action = KEYBINDS[event.key]
                    IS_PRESSED[action] = True
            if event.type == pygame.KEYUP:
                if event.key in KEYBINDS:
                    IS_PRESSED[KEYBINDS[event.key]] = False
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    start_screen.main()
