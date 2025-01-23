import pygame
import sys
from constants import *
from helpfull_functions import *
import main_cycle
from global_vars import difficult
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
    screen.blit(line, pygame.Rect(PLAY_BUTTON.centerx - line.get_width() // 2,
                                  PLAY_BUTTON.centery - line.get_height() // 2,
                                  PLAY_BUTTON.width, PLAY_BUTTON.height))


def draw_slider():
    pygame.draw.rect(screen, SLIDER_RECT_BIG_COLOR, SLIDER_RECT_BIG)
    pygame.draw.rect(screen, SLIDER_RECT2_COLOR, slider_rect)


def draw_start_screen():
    screen.fill(START_BACKGROUND_COLOR)
    draw_titles()
    draw_play_btn()
    draw_slider()
    pygame.display.flip()


def on_lmb_click(mouse_pos):
    global slider_is_pressed
    if SLIDER_RECT_BIG.collidepoint(*mouse_pos):
        slider_is_pressed = True
    elif PLAY_BUTTON.collidepoint(*mouse_pos):
        change_difficulty()
        main_cycle.main(screen)


def move_slider(ok):
    if not ok:
        return
    left = SLIDER_RECT_BIG.x
    right = SLIDER_RECT_BIG.right - SLIDER_RECT2.width
    slider_rect.x = cut_num(left, pygame.mouse.get_pos()[0] - slider_rect.width // 2, right)


def change_difficulty():
    global difficult
    d = slider_rect.centerx - SLIDER_RECT_BIG.left
    d /= SLIDER_RECT_BIG.width
    d = 1 - d
    d *= 5
    difficult = d
    print(d)
    print(difficult)


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
