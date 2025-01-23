import pygame
NULL_RECT = pygame.rect.Rect(0, 0, 0, 0)
CLOCK = pygame.time.Clock()
PLAYER_SPEED = 400
SCREEN_SIZE = (480, 720)
KEYBINDS = {119: 'up', 97: 'left', 115: 'down', 100: 'right',
            1073741906: 'up', 1073741904: 'left', 1073741905: 'down', 1073741903: 'right'}
IS_PRESSED = {'up': False, 'left': False, 'down': False, 'right': False}
FPS = 60
BACKGROUND_COLOR = '#003333'
GAME_NAME = 'Dodge the Creeps!'
GAME_NAME_COLOR = '#00aa44'
GAME_NAME_FONT_SIZE = 60
PLAY_BUTTON_TEXT = 'Play'
PLAY_BUTTON_TEXT_SIZE = 60
PLAY_BUTTON_TEXT_COLOR = GAME_NAME_COLOR


def create_rect(center, size):
    return pygame.Rect(center[0] - size[0] // 2, center[1] - size[1] // 2, *size)


PLAY_BUTTON = create_rect([int(SCREEN_SIZE[0] * 0.5), int(SCREEN_SIZE[1] * 0.85)],
                          [int(SCREEN_SIZE[0] * 0.4), int(SCREEN_SIZE[1] * 0.1)])
PLAY_BUTTON_COLOR = '#00009a'

SLIDER_RECT_BIG = create_rect([int(SCREEN_SIZE[0] * 0.5), int(SCREEN_SIZE[1] * 0.6)],
                              [int(SCREEN_SIZE[0] * 0.8), int(SCREEN_SIZE[1] * 0.04)])
SLIDER_RECT_BIG_COLOR = '#550022'

SLIDER_RECT2 = create_rect([int(SCREEN_SIZE[0] * 0.35), int(SCREEN_SIZE[1] * 0.6)],
                           [int(SCREEN_SIZE[0] * 0.1), int(SCREEN_SIZE[1] * 0.04)])
SLIDER_RECT2_COLOR = '#555500'

DIFFICULTY = 'Difficulty'
DIFFICULTY_FONT_SIZE = 40
DIFFICULTY_COLOR = GAME_NAME_COLOR
