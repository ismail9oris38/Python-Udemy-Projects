from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 25, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.value = 1
        self.goto(-230,260)
        self.write(f"Level: {self.value}",False,align=ALIGNMENT, font=FONT)
        
          
    def value_increase(self):
        self.clear()
        self.value += 1
        self.write(f"Level: {self.value}",False,align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,align=ALIGNMENT, font=FONT)
    