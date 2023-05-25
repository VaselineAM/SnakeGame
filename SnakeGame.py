from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

myscreen = Screen()
myscreen.setup(600,600)
myscreen.bgcolor('black')
myscreen.tracer(0)

food = Food()

snakebody = []

snake = Snake()
score = 0
scoreboard = ScoreBoard()

is_on = True
while is_on:
    snake.move()
    myscreen.onkey(snake.moveleft,"Left")
    myscreen.onkey(snake.moveright, "Right")
    myscreen.onkey(snake.moveup, "Up")
    myscreen.onkey(snake.movedown, "Down")

    snakehead = snake.snakebody[0]
    snaketail = snake.snakebody[len(snakebody)-1]

    if snakehead.distance(food.food)<=15:
        scoreboard.scorecard(score)
        food.refresh()
        snake.addbody()
        score = score+1
    
    xposition = snakehead.xcor()
    yposition = snakehead.ycor()

    if xposition>=290 or yposition>=290 or xposition<=-290 or yposition<=-290:
        is_on=False
        print("You lose.")
    for body in snake.snakebody[1:]:
        if snakehead.distance(body)<1:
            print("Game over")

    myscreen.listen()
    myscreen.update()

myscreen.mainloop()