from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self, snake):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh(snake)

    def refresh(self, snake):
        self.goto(self.find_spot(snake))

    @staticmethod
    def find_spot(snake):
        while True:
            random_x = randrange(-280, 281, 10)
            random_y = randrange(-280, 281, 10)

            for segment in snake:
                if segment.distance(random_x, random_y) < 10:
                    break
            else:
                return random_x, random_y
