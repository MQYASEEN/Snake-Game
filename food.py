from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.refresh_food()

    def refresh_food(self):
        xloc=random.randint(-270,270)
        yloc=random.randint(-270,270)
        self.goto(xloc,yloc)
    
