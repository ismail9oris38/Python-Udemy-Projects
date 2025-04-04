from turtle import Screen
import time
from racket import Racket
from ball import Ball
from score_board import Score

r_racket = Racket(350)
l_racket = Racket(-350)
ball = Ball()
score = Score()

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.textinput(title="Pong Game",prompt="Start")
screen.title("Pong Game")
screen.tracer(0)


screen.listen() 
screen.onkey(r_racket.up,"Up")
screen.onkey(r_racket.down,"Down")
screen.onkey(l_racket.up,"w")
screen.onkey(l_racket.down,"s")

game_is_on = True

while game_is_on:
    
    ball.move() 
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_exchange()

    if (ball.xcor() > 330 and ball.distance(r_racket) < 50)  or (ball.xcor() < -330 and ball.distance(l_racket) < 50):
        ball.x_exchange()
        ball.speed_up()

    if ball.xcor() > 360 :
        time.sleep(1)
        score.l_point()
        ball.miss()
        ball.refresh()
        
        
    if ball.xcor() < -370:
        time.sleep(1)
        score.r_point()
        ball.miss()
        ball.refresh()

    screen.update()
screen.exitonclick()