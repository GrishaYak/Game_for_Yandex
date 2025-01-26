import pygame
from helpfull_functions import *
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [load_image(el) for el in ['player1.png', 'player2.png']]
        self.a_id = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.move(PLAYER_START_POS)
        self.mask = pygame.mask.from_surface(self.image)

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = self.images[self.a_id]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args, **kwargs):
        velocity = pygame.Vector2(0, 0)
        for event in args:
            if event.type == pygame.KEYDOWN:
                if KEYBINDS[event.key] == 'up':
                    velocity.y -= 1
                if KEYBINDS[event.key] == 'down':
                    velocity.y += 1
                if KEYBINDS[event.key] == 'left':
                    velocity.x -= 1
                if KEYBINDS[event.key] == 'right':
                    velocity.x += 1
        velocity.normalize()
        self.rect.move(velocity * PLAYER_SPEED)
        self.rect.clamp(pygame.Rect(0, 0, *SCREEN_SIZE))


# pygame.init()
# screen = pygame.display.set_mode(SCREEN_SIZE)
# a = Player()
