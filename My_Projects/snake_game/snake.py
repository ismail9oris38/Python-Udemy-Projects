from turtle import Turtle
  
class Snake:
    def __init__(self): 
        self.all_snake = []
        self.create_tail()
        self.head = self.all_snake[0]
        
       
    
    def create_tail(self):
        x = 0
        for _ in range(3):
            self.tail_adding(x,0)
        x -= 20
        
    def tail_adding(self,x,y):
        tail = Turtle(shape="square")
        tail.color("white")
        tail.penup()
        tail.goto(x,y)

        self.all_snake.append(tail)
              
        
    def extend(self):
        x, y = self.all_snake[-1].xcor(), self.all_snake[-1].ycor()
        self.tail_adding(x,y)
        

    def move(self): 
        for i in range(len(self.all_snake) - 1, 0, -1):
            x,y = self.all_snake[i-1].pos()
            self.all_snake[i].goto(x,y)

        self.head.forward(20)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            
   
        
