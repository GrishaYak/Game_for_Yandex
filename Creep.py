import pygame
from constants import *
from helpfull_functions import load_image
from random import randint


class Creep(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.degree = 0
        img_name = 'enemy' + str(randint(1, 3)) + '_'
        self.images = [load_image(el) for el in [img_name + '1.png', img_name + '2.png']]
        self.a_id = 1
        self.a_cnt = 0
        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.a_change()
        self.start_pos = pygame.Vector2()
        self.direction = pygame.Vector2()
        self.generate_start_pos_dir()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.start_pos)

    def generate_start_pos_dir(self):
        self.degree = randint(0, 359)
        x = randint(1, int(SCREEN_SIZE.x - self.image.get_width() - 2))
        y = randint(0, int(SCREEN_SIZE.y - self.image.get_height() - 2))
        if 315 <= self.degree or self.degree < 45:
            self.start_pos = [x, SCREEN_SIZE.y - self.image.get_height() - 2]
        elif 45 <= self.degree < 135:
            self.start_pos = [0, y]
        elif 135 <= self.degree < 225:
            self.start_pos = [x, 0]
        else:
            self.start_pos = [SCREEN_SIZE.x - self.image.get_width() - 2, y]
        self.direction = pygame.Vector2(0, -1).rotate(self.degree)

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = self.images[self.a_id]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.image = pygame.transform.rotate(self.image, self.degree)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args, **kwargs):
        self.rect = self.rect.move(self.direction * PLAYER_SPEED)
        self.a_cnt += 1
        if self.a_cnt == 10:
            self.a_cnt = 0
            self.a_change()
