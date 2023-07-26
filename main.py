from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width = 800)
screen.title("PONG GAME")
screen.tracer(0)

paddle_r = Paddle()
paddle_l = Paddle()
paddle_r.create_paddle(350)
paddle_l.create_paddle(-350)
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

ball = Ball()
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.update_lscore()

    if ball.xcor() < -380:
        ball.ball_reset()
        score.update_rscore()


















screen.exitonclick()