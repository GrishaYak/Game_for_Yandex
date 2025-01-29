import pygame
import sys
import json
from Creep import Creep
from constants import *
from helpfull_functions import *
from Player import Player

screen = pygame.display.set_mode(SCREEN_SIZE)
score = SCORE


def draw_game_over():
    font = pygame.font.Font(None, GAME_OVER_SIZE)
    line = font.render(GAME_OVER, True, GAME_OVER_COLOR)
    rect = pygame.Rect((SCREEN_SIZE.x - line.get_width()) // 2,
                       (SCREEN_SIZE.y - line.get_height()) // 2, *line.get_size())
    screen.blit(line, rect)


def build():
    screen.fill(MAIN_BACKGROUND_COLOR)
    pygame.display.flip()


def draw_the_score():
    font = pygame.font.Font(None, SCORE_FONT)
    line = font.render(str(score), True, SCORE_COLOR)
    rect = pygame.Rect((SCREEN_SIZE.x - line.get_width()) // 2, SCREEN_SIZE.y * 0.05 - line.get_height() // 2,
                       *line.get_size())
    screen.blit(line, rect)


def draw_best_score(best_score):
    font = pygame.font.Font(None, BEST_SCORE_FONT)
    line = font.render(BEST_SCORE + str(best_score), True, BEST_SCORE_COLOR)
    rect = pygame.Rect((SCREEN_SIZE.x - line.get_width()) // 2, SCREEN_SIZE.y * 0.12 - line.get_height() // 2,
                       *line.get_size())
    screen.blit(line, rect)


def check(rect: pygame.Rect):
    if rect.right < 0 or rect.left > SCREEN_SIZE.x:
        return True
    if rect.bottom < 0 or rect.top > SCREEN_SIZE.y:
        return True
    return False


def main(difficult):
    global screen, score
    creeps = pygame.sprite.Group()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    SPAWN_THE_CREEP = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_THE_CREEP, int(difficult * 1000) * 2)
    score = 0
    bg_music = pygame.mixer.Sound('art/music.ogg')
    bg_music.play(-1)
    gameover_sound = pygame.mixer.Sound('art/gameover.wav')
    pygame.mixer.music.set_volume(0.1)
    player = Player()
    while True:
        events = pygame.event.get()
        with open('data.json') as f:
            best_score = json.load(f)
        if score > best_score:
            best_score = score
            with open('data.json', 'w') as f:
                json.dump(score, f)
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key in KEYBINDS:
                    action = KEYBINDS[event.key]
                    IS_PRESSED[action] = True
            if event.type == pygame.KEYUP:
                if event.key in KEYBINDS:
                    IS_PRESSED[KEYBINDS[event.key]] = False
            if event.type == SPAWN_THE_CREEP:
                Creep(creeps)
        if player.update(creeps):
            break
        creeps.update()
        creeps_to_delete = []
        for creep in creeps:
            if check(creep.rect):
                creeps_to_delete.append(creep)
        score += len(creeps_to_delete)
        for creep in creeps_to_delete:
            creeps.remove(creep)
        screen.fill(MAIN_BACKGROUND_COLOR)
        screen.blit(player.image, (player.rect.x, player.rect.y))
        creeps.draw(screen)
        clock.tick(FPS)
        draw_the_score()
        draw_best_score(best_score)
        pygame.display.flip()
    bg_music.stop()
    if score > best_score:
        with open('data.json', 'w') as f:
            json.dump(score, f)
    pygame.time.wait(250)
    draw_game_over()
    gameover_sound.play()
    pygame.display.flip()
    pygame.time.wait(2000)


if __name__ == '__main__':
    pygame.init()
