from operator import truediv
from random import Random
from turtle import *
from boll import Ball
from padle import Padles
import time
from scorebord import Scoreboard
screen = Screen()
screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)



r_padle = Padles((350, 0))
l_padle = Padles((-350,0))
ball = Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_padle.on_up , "Up")
screen.onkey(r_padle.on_down, "Down")
screen.onkey(l_padle.on_up2, "a")
screen.onkey(l_padle.on_down2, "s")


game_on = True        
while game_on  :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #print(r_padle.distance(ball))

   
     
     
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()
        
    
    if ball.distance(r_padle)  <50 and ball.xcor() >325:
        ball.bounce_x()
    
    if ball.distance(l_padle)  <50 and ball.xcor() >-355:
        ball.bounce_x()
        
    if ball.xcor() > 380 :
        ball.stop() 
        score.r_point()
        
    if ball.xcor() < -400 :
        ball.stop()
        score.l_point()
        #scoreboard.r_point(scoreboard)
    #  if ball.xcor() <= -400 or ball.xcor() >=380:
    #   print(f" YOUR {ball.l_score}:{ball.r_score}")  
        
         
    #  if ball.xcor() >380 or ball.xcor() < -400:
        
        
screen.exitonclick()