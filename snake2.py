from turtle import Turtle, Screen

import random
import time

class Snake:
    def __init__(self):
        self.turtles = []
        self.positions = [(-40,0), (-20,0), (0,0), (20,0), (40,0), (60,0), (80,0)]
        self.create_snake()
        self.head = self.turtles[-1]

    def create_snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles) - 1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)
    
    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_segment)
        #.append(object)
        #insert(index, object)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)    