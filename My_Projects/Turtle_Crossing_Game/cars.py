from turtle import Turtle
from random import randint,choice

colors = [
    "red", "green", "blue", "yellow", "purple", "orange", "pink", "black",
    "brown", "cyan", "magenta", "teal", "olive", "maroon", "navy", "lime", "gold", "silver",
    "indigo", "violet", "beige", "coral", "turquoise", "salmon", "khaki", "crimson"
]


class Cars:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        
    def create_car(self):
        for i in range(25):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(1,2)
            car.setheading(180)
            car.color(choice(colors))
            rand_x = randint(300,800)
            rand_y = randint(-240,260)
            car.goto(rand_x,rand_y)
            self.all_cars.append(car)
            self.speed = 1
            
    def move(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                rand_x = randint(320,800)
                rand_y = randint(-250,250)
                car.goto(rand_x,rand_y)
                
            new_x = car.xcor() - self.speed
            y = car.ycor()
            car.goto(new_x,y)

    def cars_speed(self):
        self.speed += 1