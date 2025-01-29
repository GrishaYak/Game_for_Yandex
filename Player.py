import pygame
from helpfull_functions import *
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [load_image(el) for el in ['player1.png', 'player2.png']]
        self.a_counter = 0
        self.a_id = 1
        self.image = self.images[0]
        self.a_change()
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(PLAYER_START_POS.x - self.rect.width // 2, PLAYER_START_POS.y - self.rect.height // 2,
                                self.rect.w, self.rect.h)
        self.mask = pygame.mask.from_surface(self.image)

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = self.images[self.a_id]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, creeps):
        if self.a_counter >= 15:
            self.a_counter = 0
            self.a_change()
        velocity = pygame.Vector2(0, 0)
        if IS_PRESSED['up']:
            velocity.y -= 1
        if IS_PRESSED['down']:
            velocity.y += 1
        if IS_PRESSED['left']:
            velocity.x -= 1
        if IS_PRESSED['right']:
            velocity.x += 1
        if velocity.x or velocity.y:
            self.a_counter += 1
            velocity = velocity.normalize()
        self.rect = self.rect.move(velocity * PLAYER_SPEED)
        self.rect = self.rect.clamp(0, 0, *SCREEN_SIZE)
        for creep in creeps:
            if pygame.sprite.collide_mask(self, creep) is not None:
                return True
        return False

# pygame.init()
# screen = pygame.display.set_mode(SCREEN_SIZE)
# a = Player()
