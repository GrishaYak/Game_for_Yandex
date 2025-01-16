import os
import sys
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('art', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image.convert_alpha()


def belongs_to(point, rect1: pygame.Rect):
    return 0 < point[0] - rect1.x < rect1.width and 0 < point[1] - rect1.y < rect1.height


def cut_num(left_divide, num, right_divide):
    if num < left_divide:
        return left_divide
    if num > right_divide:
        return right_divide
    return num
