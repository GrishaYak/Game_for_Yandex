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
        print(self.rect.size)
        self.mask = pygame.mask.from_surface(self.image)

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = self.images[self.a_id]

    def update(self, *args, **kwargs):
        velocity = pygame.Vector2(0, 0)
        for event in args:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    velocity.y -= 1
                if event.key == pygame.K_s:
                    velocity.y += 1
                if event.key == pygame.K_a:
                    velocity.x -= 1
                if event.key == pygame.K_d:
                    velocity.x += 1
        velocity.normalize()
        self.rect.move(velocity * PLAYER_SPEED)


# pygame.init()
# screen = pygame.display.set_mode(SCREEN_SIZE)
# a = Player()
