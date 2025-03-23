from turtle import Screen, Turtle
from snake2 import Snake
import time
from food import Food
from scoreboard import Score


window = Screen()
window.setup(height= 800, width= 800)
window.title("Snake game")
window.tracer(0)
window.bgcolor("black")

sam = Snake()
food = Food()
score = Score()

game_on = True

while game_on:
    sam.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up, "Up")
    window.onkey(sam.down, "Down") 
    window.onkey(sam.right, "Right")
    window.onkey(sam.left, "Left")
    if sam.head.distance(food) < 15:
        food.appear()
        sam.extend()
        score.increase_score()

    if sam.head.xcor() > 370 or sam.head.xcor() < -370 or sam.head.ycor() > 370 or sam.head.ycor() < -370:
        game_on = False
        score.game_over()

    for segment in sam.turtles[:-1]:
        if sam.head.distance(segment) < 10:
            game_on = False
            score.game_over()
     

window.exitonclick()    

# slicing 
# part = part[start:end:step]
# list = [0,1,2,3,4,5,6,7] if want to print all items minus the last one => list[0:-1] => as he's by default starts by index 0 then => list[:-1]