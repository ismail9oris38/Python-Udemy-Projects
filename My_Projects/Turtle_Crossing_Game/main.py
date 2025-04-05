from turtle import Screen
import time
from my_shape import My_shape
from cars import Cars
from score_board import Score

screen = Screen()
screen.bgcolor("gray")
screen.setup(600,600)
screen.textinput(title="Game",prompt="start")
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle = My_shape()
cars = Cars()
score = Score()

screen.listen()
screen.onkey(turtle.up,"Up")
screen.onkey(turtle.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    cars.move()
    
    if turtle.ycor() > 280:
        time.sleep(1)
        turtle.refresh()
        cars.cars_speed()
        score.value_increase()
        
        
    for car in cars.all_cars:
        if turtle.distance(car) < 20 :
            time.sleep(1)
            score.game_over()
            game_is_on = False
                 
screen.exitonclick()