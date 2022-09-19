from turtle import Turtle
from random import Random

class Ball(Turtle):

    def __init__(self ):
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
        
    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new ,y_new)
        
    def bounce (self):
        self.y_move *= - 1
    def bounce_x (self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def stop (self) :
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x() 
        
        
    