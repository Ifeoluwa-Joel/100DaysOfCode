import random
from turtle import Screen
from snake import Snake
from food import Food, BonusBall
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
bonus_ball = BonusBall()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        chance = random.randint(1, 5)  # Use to control num of times the Bonus will show up. LOGIC DOWN TO LINE 35
        if chance == 1:
            bonus_ball.refresh()
        snake.extend()
        scoreboard.increase_score()
        food.refresh()
    if snake.head.distance(bonus_ball) < 15:
        scoreboard.increase_bonus_score()
        bonus_ball.go_off_screen()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_()
        snake.reset()
        food.refresh()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_()
            snake.reset()
            food.refresh()

screen.exitonclick()
