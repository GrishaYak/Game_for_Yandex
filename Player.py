from Object import Object
def move_by_decorator(func):


class Player(Object):
    def __init__(self, pos):
        super().__init__(pos, 'playerGrey_up1.png')
        self.is_moving = True

