import pygame
import sys
from constants import *
from helpfull_functions import *
import start_screen
from global_vars import difficult


class Animation:
    def __init__(self, *names):
        self.images = [load_image(el) for el in names]
        self.id = 0

    def swap(self):
        self.id = (self.id + 1) % len(self.images)

    def get(self):
        return self.images[self.id]


player = pygame.Surface(PLAYER_SIZE)
player_animation = Animation('player1.png', 'player2.png')
all_sprites = pygame.sprite.Group()


def build(screen):
    print(difficult)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("bomb.png")
    screen.fill(MAIN_BACKGROUND_COLOR)
    screen.blit(player, PLAYER_START_POS)
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
        screen.blit(player)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    start_screen.main()
