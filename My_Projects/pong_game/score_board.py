from turtle import Turtle

ALİGNMENT = "center"
FONT = ('courier', 70, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreBoard()
        self.line()
        
    def update_scoreBoard(self):  
        self.goto(-50,220)
        self.write(self.l_score,align=ALİGNMENT,font=FONT)
        self.goto(50,220)
        self.write(self.r_score,align=ALİGNMENT,font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreBoard()
        
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreBoard()
    
    def line(self):
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.2, stretch_len=1.5)

        for _ in range(30):
            self.stamp()
            self.forward(50)
            
            
    