from turtle import Turtle

class Racket(Turtle):
    def __init__(self,start_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(start_cor,0)
        self.x = start_cor

        
        
    def up(self):
        y = self.ycor() + 20
        self.goto(self.x,y)
        
    def down(self):
        y = self.ycor() - 20
        self.goto(self.x,y)
        
            