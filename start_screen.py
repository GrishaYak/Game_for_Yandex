import pygame
import sys
from constants import *
from helpfull_functions import *
surfaces = {'play_btn': NULL_RECT, 'slider': NULL_RECT}


def draw_title(screen):
    font = pygame.font.Font(None, 60)
    line = font.render(GAME_NAME, True, GAME_NAME_COLOR)
    rect = line.get_rect()
    rect.y = 50
    rect.x = (SCREEN_SIZE[0] - line.get_width()) // 2
    screen.blit(line, rect)


def draw_play_btn(screen):
    font = pygame.font.Font(None, 60)
    line = font.render(PLAY_BUTTON_TEXT, True, PLAY_BUTTON_COLOR)


def draw_start_screen(screen):
    draw_title(screen)


def main(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == 1:
                on_left_button_click()
        draw_start_screen(screen)


if __name__ == '__main__':
    pygame.init()
    main(pygame.display.set_mode(SCREEN_SIZE))
