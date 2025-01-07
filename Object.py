import numpy as np
from helpfull_functions import load_image


class Object:
    def __init__(self, position=None, image_name=''):
        if position is None:
            position = np.array([0.0, 0.0])
        self.pos = np.array(position)
        self.change_sprite(image_name)

    def change_sprite(self, image_name):
        if image_name:
            self.image = load_image(image_name)

    def set_pos(self, pos: tuple):
        self.pos = np.array(pos)

    def get_pos(self):
        return self.pos

    def move_by(self, vector):
        self.pos += vector
