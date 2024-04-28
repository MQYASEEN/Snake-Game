from turtle import Turtle

ALIGN='center'
FONT=('Arial',12,'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score=0
        self.scoreboard()
    def scoreboard(self):
        self.goto(0,260)
        self.write(f'Score : {self.score}',True,align=ALIGN,font=FONT)

    def update_score(self):
        self.score+=10
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over',True,align='center',font=('Arial',22,'bold'))