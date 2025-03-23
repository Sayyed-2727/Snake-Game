# The main code

from turtle import Turtle, Screen
from snake import Snake
import time

window = Screen()
window.setup(width= 1200, height= 800)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

sam = Snake()

game_on = True
 
while game_on:
    sam.move_snake()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up,"Up")
    window.onkey(sam.down, "Down")
    window.onkey(sam.right, "Right")
    window.onkey(sam.left, "Left")
window.exitonclick()