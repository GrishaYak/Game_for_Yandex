import pygame
from classes import Border
from constants import *

difficult = 0.5
all_sprites = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
top_border = Border(0, 0, SCREEN_SIZE[0], 0)
bottom_border = Border(0, SCREEN_SIZE[1], SCREEN_SIZE[0], SCREEN_SIZE[1])
left_border = Border(0, 0, 0, SCREEN_SIZE[1])
right_border = Border(SCREEN_SIZE[0], 0, SCREEN_SIZE[0], SCREEN_SIZE[1])