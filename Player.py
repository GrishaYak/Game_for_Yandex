import pygame
from helpfull_functions import *
from constants import *
from global_vars import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [load_image(el) for el in ['player1.png', 'player2.png']]
        self.a_id = 1
        self.image = self.images[1]
        self.a_change()
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(PLAYER_START_POS.x - self.rect.width // 2, PLAYER_START_POS.y - self.rect.height // 2,
                                self.rect.w, self.rect.h)
        self.mask = pygame.mask.from_surface(self.image)

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = pygame.transform.scale(self.images[self.a_id], (SCREEN_SIZE // 8))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args, **kwargs):
        velocity = pygame.Vector2(0, 0)
        for event in args:
            if event.type == pygame.KEYDOWN:
                if event.key not in KEYBINDS.keys():
                    continue
                print(KEYBINDS[event.key])
                if KEYBINDS[event.key] == 'up':
                    velocity.y -= 1
                if KEYBINDS[event.key] == 'down':
                    velocity.y += 1
                if KEYBINDS[event.key] == 'left':
                    velocity.x -= 1
                if KEYBINDS[event.key] == 'right':
                    velocity.x += 1
        if velocity.x and velocity.y:
            velocity.normalize()
        self.rect.move(velocity * PLAYER_SPEED)
        self.rect.clamp(pygame.Rect(0, 0, *SCREEN_SIZE))
        for creep in creeps:
            if pygame.sprite.collide_mask(self, creep):
                return True
        return False

# pygame.init()
# screen = pygame.display.set_mode(SCREEN_SIZE)
# a = Player()
