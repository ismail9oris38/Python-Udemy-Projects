from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 15, 'normal')
FONT_BIG = ('courier', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-20,280)
        self.write(f"Score: {self.value}",False,align=ALIGNMENT, font=FONT)
        
          
    def value_increase(self):
        self.clear()
        self.value += 1
        self.write(f"Score: {self.value}",False,align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,align=ALIGNMENT, font=FONT_BIG)
