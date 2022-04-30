from re import S
import turtle

#open windows 

wis = turtle.Screen()
wis.title("pong by krism")
wis.bgcolor("black")
wis.setup(width = 800, height = 600)
wis.tracer(0)

#Player A
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("blue")
playerA.penup()
playerA.goto(-350, 0)
playerA.shapesize(stretch_wid = 5, stretch_len = 1)

#Player B
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("red")
playerB.penup()
playerB.goto(350, 0)
playerB.shapesize(stretch_wid = 5, stretch_len = 1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

#Line 
div = turtle.Turtle()
div.color("gray")
div.goto(0, -400)
div.goto(0, 400)

#functions

#Player A
def playerA_up():
    y = playerA.ycor()
    y += 20
    playerA.sety(y)

def playerA_down():
    y = playerA.ycor()
    y -= 20
    playerA.sety(y)

#palyer B
def playerB_up():
    y = playerB.ycor()
    y += 20
    playerB.sety(y)

def playerB_down():
    y = playerB.ycor()
    y -=20
    playerB.sety(y)

#keyboard
wis.listen()
wis.onkeypress(playerA_up, "w") 
wis.onkeypress(playerA_down, "s")
wis.onkeypress(playerB_up, "Up")
wis.onkeypress(playerB_down, "Down")

while True:
    wis.update()
