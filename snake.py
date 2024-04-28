from turtle import Turtle

UP=90
RIGHT=0
LEFT=180
DOWN=270
SNAKE_DIRECTION=[(-20,0),(0,0),(20,0)]
DISTANCE=20
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body=[]
        self.create_snake()
        self.snake_head=self.snake_body[0]

    def create_snake(self):
        for position in SNAKE_DIRECTION:
            self.add_new_part(position)
        
    def add_new_part(self,position):
        snake=Turtle(shape='square')
        snake.penup()
        snake.color('white')
        snake.goto(position)
        self.snake_body.append(snake)
    
    def extend_snake(self):
        self.add_new_part(self.snake_body[-1].position())
    
    def snake_move(self):
        for snakerange in range(len(self.snake_body)-1,0,-1):
            xloc=self.snake_body[snakerange-1].xcor()
            yloc=self.snake_body[snakerange-1].ycor()
            self.snake_body[snakerange].goto(xloc,yloc)
        self.snake_head.fd(DISTANCE)

    
    def moveup(self):
        if self.snake_head.heading()!=DOWN:
             self.snake_head.setheading(UP)

    def movedown(self):
        if self.snake_head.heading()!=UP:
             self.snake_head.setheading(DOWN)
    def moveleft(self):
        if self.snake_head.heading()!=RIGHT:
             self.snake_head.setheading(LEFT)
    def moveright(self):
        if self.snake_head.heading()!=LEFT:
             self.snake_head.setheading(RIGHT)
    