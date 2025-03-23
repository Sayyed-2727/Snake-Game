# from turtle import Turtle
# import random

# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("red")
#         self.penup()
#         self.appear()
#         self.shapesize(0.5,0.5)

#     def appear(self):
#         x_random = random.randint(-380, 380)
#         y_random = random.randint(-380,380)
#         self.goto(x_random, y_random)


from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)
        self.appear()

    def appear(self):
        x_random = random.randint(-380,380)
        y_random = random.randint(-380,380)
        self.goto(x_random,y_random)