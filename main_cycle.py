import pygame
import sys
from constants import *
from helpfull_functions import *
import start_screen
from global_vars import difficult
from Player import Player

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


def build(screen):
    print(difficult)
    screen.fill(MAIN_BACKGROUND_COLOR)
    screen.blit(player)
    pygame.display.flip()


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
        screen.fill(MAIN_BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    start_screen.main()
