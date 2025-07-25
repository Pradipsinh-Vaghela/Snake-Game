from idlelib.zoomheight import set_window_geometry
from turtle import  Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score_refresh()

    # Detect Collision with Wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        game_is_on = False

    # Detect Collision with Tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            game_is_on = False

screen.exitonclick()
