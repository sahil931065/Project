from turtle import *


class Padles(Turtle):
    # PADLE NUMBER 1
    def __init__(self,position ):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1 ,stretch_wid=5)
        self.penup()
        self.goto(position) 
        
        #PADLE 1 CONTROL     
        
    def on_up(self):
        y_new = self.ycor() +30
        self.goto(self.xcor() , y_new)
    
    def on_down(self):
        y_new = self.ycor() -30
        self.goto(self.xcor() , y_new)
        
    def on_up2(self):
        y_new = self.ycor() +30
        self.goto(self.xcor() , y_new)
        
    def on_down2(self):
        y_new = self.ycor() -30
        self.goto(self.xcor() , y_new)
        
    
    