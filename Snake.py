from turtle import Turtle

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snakebody = []
        self.create_snake()

    def create_snake(self):
        for x in range(3):
            snake = Turtle()
            snake.penup()
            snake.color('white')
            snake.shape('square')
            #20 pixels 
            snake.setx((-x*20))
            #snake.speed(4)
            self.snakebody.append(snake)  
    
    def addbody(self):
        body = Turtle()
        body.penup()
        body.color('white')
        body.shape('square')
        self.snakebody.append(body)
        

    def move(self):
        for x in range(len(self.snakebody)-1,0,-1):
            new_x = self.snakebody[x-1].xcor()
            new_y = self.snakebody[x-1].ycor()
            self.snakebody[x].goto(new_x,new_y)
        self.snakebody[0].fd(5)

    def moveright(self):
        if self.snakebody[0].heading()!=180:
            self.snakebody[0].seth(0)
    def moveleft(self):
        if self.snakebody[0].heading()!=180:
            self.snakebody[0].seth(180)
    def moveup(self):
        if self.snakebody[0].heading()!=270:
            self.snakebody[0].seth(90)
    def movedown(self):
        if self.snakebody[0].heading()!=90:
            self.snakebody[0].seth(270)