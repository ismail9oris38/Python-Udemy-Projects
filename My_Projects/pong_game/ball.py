from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_change = 2
        self.x_change = 2
        
        
    def move(self):
        x,y = self.xcor() + self.x_change, self.ycor() + self.y_change
        self.goto(x,y)
        
    def speed_up(self):
        self.y_change *= 1.2
        self.x_change *= 1.2
        
    def y_exchange(self):
        self.y_change *= -1
        
    def x_exchange(self):
        self.x_change *= -1
        
    def miss(self):
        self.goto(0,0)
        self.x_exchange()
        
    def refresh(self):
        self.y_change = 2
        self.x_change = 2