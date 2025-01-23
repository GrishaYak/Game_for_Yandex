import pygame
from helpfull_functions import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [load_image(el) for el in ['player1.png', 'player2.png']]
        self.a_id = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def a_change(self):
        self.a_id = (self.a_id + 1) % len(self.images)
        self.image = self.images[self.a_id]
