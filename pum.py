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
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


while True:
    wis.update()

#Remenber: You ara bulding a game with video on youtube, keep tomorrow.

