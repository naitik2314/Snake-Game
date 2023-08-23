from random import randint

class Food():

    def __init__(self):
        pass

    def position(self):
        self.x_position_food = randint(-300, 300)
        self.y_position_food = randint(-300, 300)