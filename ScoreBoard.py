from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,280)
        self.pencolor('white')
        self.ht()

    def scorecard(self,score):
        self.clear()
        self.write(f"Score: {score}",False,"center",("Arial",18,"normal"))
        
        
        