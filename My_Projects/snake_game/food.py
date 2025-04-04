from turtle import Turtle,Screen
from random import randint


class Food(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = randint(-270,270)
        random_y = randint(-270,270)
        self.goto(random_x,random_y)
