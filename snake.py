# Snake Class
# Method: Create Snake
# Method: Move Snake

from turtle import Turtle, Screen
import random
import time

class Snake:
    def __init__(self):
        self.turtles = []
        self.positions = [(-40,0), (-20,0) , (0,0), (20,0), (40,0), (60,0), (80,0)]
        self.colors = ["red", "brown", "blue", "yellow", "cyan", "green", "white"]
        self.angles = (0,0,0,90)
        self.create_snake()
    
    def create_snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            new_turtle.color("white")
            self.turtles.append(new_turtle) 

    def move_snake(self):
        for i in range(len(self.turtles) -1):
            self.turtles[i].goto(self.turtles[i +1].pos())
        self.turtles[-1].forward(20) 
    def up(self):
        self.turtles[-1].setheading(90)
    def down(self):
        self.turtles[-1].setheading(270)
    def right(self):
        self.turtles[-1].setheading(0)
    def left(self):
        self.turtles[-1].setheading(180)