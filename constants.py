import pygame
PLAYER_SPEED = 400
SCREEN_SIZE = (480, 720)
KEYBINDS = {119: 'up', 97: 'left', 115: 'down', 100: 'right',
            1073741906: 'up', 1073741904: 'left', 1073741905: 'down', 1073741903: 'right'}
IS_PRESSED = {'up': False, 'left': False, 'down': False, 'right': False}
FPS = 60
BACKGROUND_COLOR = '#171717'
GAME_NAME = 'Dodge the Creeps!'
GAME_NAME_COLOR = '#dddddd'
PLAY_BUTTON_TEXT = 'Play'
PLAY_BUTTON_COLOR = '#dddddd'
NULL_RECT = pygame.rect.Rect(0, 0, 0, 0)