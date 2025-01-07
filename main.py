import pygame
from constants import *


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in KEYBINDS:
                    action = KEYBINDS[event.key]
                    IS_PRESSED[action] = True
            if event.type == pygame.KEYUP:
                if event.key in KEYBINDS:
                    IS_PRESSED[KEYBINDS[event.key]] = False

        if any(IS_PRESSED.values()):
            screen.fill('#888888')
        else:
            screen.fill('#000000')
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    main()
