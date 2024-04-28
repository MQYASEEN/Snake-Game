from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
screen.onkey(snake.moveup,'Up')
screen.onkey(snake.movedown,'Down')
screen.onkey(snake.moveleft,'Left')
screen.onkey(snake.moveright,'Right')

food=Food()
scoreboard=Scoreboard()
game_on=True
while game_on:
    snake.snake_move()
    time.sleep(0.1)
    #detect food eating
    if snake.snake_head.distance(food)<20:
        food.refresh_food()
        scoreboard.update_score()
        snake.extend_snake()
    #detect collision with walls 
    if snake.snake_head.xcor()>280 or snake.snake_head.ycor()>280 or snake.snake_head.xcor()<-280 or snake.snake_head.ycor()<-280:
        game_on=False
        scoreboard.game_over()
    
    #detect collision with own tail
    for parts in snake.snake_body[3:]:
        if parts.distance(snake.snake_head)<20:
            game_on=False
            scoreboard.game_over()


    screen.update()

screen.exitonclick()