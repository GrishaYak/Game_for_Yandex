import pygame
from constants import *
from helpfull_functions import load_image
from random import randint, shuffle


class Creep(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        img_name = 'enemy' + str(randint(1, 3)) + '_'
        self.images = [load_image(el) for el in [img_name + '1.png', img_name + '2.png']]
        self.a_id = 0
        self.start_pos = pygame.Vector2()
        self.direction = pygame.Vector2()
        self.generate_start_pos_dir()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.move(self.start_pos)
        self.mask = pygame.mask.from_surface(self.image)

    def generate_start_pos_dir(self):
        a = [0, 1]
        shuffle(a)
        for i in range(2):
            el = a[i]
            if el == 0:
                self.start_pos[i] = randint(0, 1) * SCREEN_SIZE[i]
                self.direction[i] = ((self.start_pos[i] == 0) - 0.5) * 2
            else:
                self.start_pos[i] = randint(0, SCREEN_SIZE[i] - 1)
        self.direction.rotate(randint(-45, 45))

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = self.images[self.a_id]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args, **kwargs):
        self.rect.move(self.direction * PLAYER_SPEED)
