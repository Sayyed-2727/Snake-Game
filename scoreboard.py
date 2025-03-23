from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()        
        self.goto(x=0,y=350)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align= "center", font=('Arial', 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        self.write(f"Game over\nFinal score: {self.score}", align= "center", font=("arial", 20, "normal"))