from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgpic(picname='fantastic-sports.gif')
screen.setup(width=800, height=600)
screen.title("Ping-Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
left_player_score = Scoreboard((-100, 200))
right_player_score = Scoreboard((100, 200))

screen.listen()
screen.onkeypress(right_paddle.go_up, 'Up')
screen.onkeypress(right_paddle.go_down, 'Down')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #  Detect collision with top & bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Detect when paddle missed the ball
    if ball.xcor() > 350:
        ball.reset_position()
        left_player_score.update_score()

    elif ball.xcor() < -350:
        ball.reset_position()
        right_player_score.update_score()

screen.exitonclick()
