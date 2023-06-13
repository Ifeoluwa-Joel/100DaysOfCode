from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)

billy = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=billy.up, key="Up")
screen.onkey(fun=billy.down, key="Down")
screen.onkey(fun=billy.left, key="Left")
screen.onkey(fun=billy.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    billy.move()

    # Detecting collision with the food
    if billy.snakehead.distance(food) < 15:
        food.refresh()
        billy.extend()
        scoreboard.increase_score()

    # Detecting collision with the wall
    if billy.snakehead.xcor() > 280 or billy.snakehead.xcor() < -280 or billy.snakehead.ycor() > 280\
            or billy.snakehead.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detecting collision with tail
    for segment in billy.segments[1:]:
        if billy.snakehead.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
