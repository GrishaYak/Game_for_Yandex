import pygame
import sys
from constants import *
from helpfull_functions import *
import started_game
surfaces = {'play_btn': NULL_RECT, 'slider': NULL_RECT}
slider_is_pressed = False
slider_rect = SLIDER_RECT2.copy()


def draw_titles():
    font = pygame.font.Font(None, GAME_NAME_FONT_SIZE)
    line = font.render(GAME_NAME, True, GAME_NAME_COLOR)
    rect = pygame.Rect((SCREEN_SIZE[0] - line.get_width()) // 2, 50, *line.get_size())
    screen.blit(line, rect)

    font = pygame.font.Font(None, DIFFICULTY_FONT_SIZE)
    line = font.render(DIFFICULTY, True, DIFFICULTY_COLOR)
    rect = pygame.Rect((SCREEN_SIZE[0] - line.get_width()) // 2, SLIDER_RECT2[1] - 40,
                       *line.get_size())
    screen.blit(line, rect)


def draw_play_btn():
    pygame.draw.rect(screen, PLAY_BUTTON_COLOR, PLAY_BUTTON)
    font = pygame.font.Font(None, 60)
    line = font.render(PLAY_BUTTON_TEXT, True, PLAY_BUTTON_TEXT_COLOR)
    screen.blit(line, pygame.Rect(PLAY_BUTTON.x + line.get_width() // 2, PLAY_BUTTON.y + line.get_height() // 2,
                                  PLAY_BUTTON.width, PLAY_BUTTON.height))


def draw_slider():
    pygame.draw.rect(screen, SLIDER_RECT1_COLOR, SLIDER_RECT1)
    pygame.draw.rect(screen, SLIDER_RECT2_COLOR, slider_rect)


def draw_start_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_titles()
    draw_play_btn()
    draw_slider()
    pygame.display.flip()


def on_lmb_click(mouse_pos):
    global slider_is_pressed
    if belongs_to(mouse_pos, SLIDER_RECT1):
        slider_is_pressed = True
    elif belongs_to(mouse_pos, PLAY_BUTTON):
        started_game.main(screen)


def move_slider(ok):
    if not ok:
        return
    left = SLIDER_RECT1.x
    right = SLIDER_RECT1.right - SLIDER_RECT2.width
    slider_rect.x = cut_num(left, pygame.mouse.get_pos()[0] - slider_rect.width // 2, right)


def main():
    global slider_is_pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if pygame.mouse.get_pressed()[0]:
                on_lmb_click(pygame.mouse.get_pos())
            else:
                slider_is_pressed = False
        move_slider(slider_is_pressed)
        draw_start_screen()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    main()
