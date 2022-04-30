
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
playerA.goto(-610, 0)
playerA.shapesize(stretch_wid = 8, stretch_len = 1)

#Player B
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("red")
playerB.penup()
playerB.goto(610, 0)
playerB.shapesize(stretch_wid = 8, stretch_len = 1)

#ball
ball = turtle.Turtle()
ball.speed(0.1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

#Line 
div = turtle.Turtle()
div.color("gray")
div.goto(0, -400)
div.goto(0, 400)

#pluma
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0       Player B: 0", align = "center", font=("courier", 20, "normal"))

#scoreboard
score_A = 0
score_B = 0

###functions

#Player A
def playerA_up():
    y = playerA.ycor()
    y += 30
    playerA.sety(y)

def playerA_down():
    y = playerA.ycor()
    y -= 30
    playerA.sety(y)

#palyer B
def playerB_up():
    y = playerB.ycor()
    y += 30
    playerB.sety(y)

def playerB_down():
    y = playerB.ycor()
    y -= 30
    playerB.sety(y)

#keyboard
wis.listen()
wis.onkeypress(playerA_up, "w") 
wis.onkeypress(playerA_down, "s")
wis.onkeypress(playerB_up, "Up")
wis.onkeypress(playerB_down, "Down")

while True:
    wis.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
        
#bords 
    if ball.ycor() > 360:
        ball.dy *= -1
    if ball.ycor() < -360:
        ball.dy *= -1
    
#bords right and left
    if ball.xcor() > 790:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_A, score_B), align = "center", font=("courier", 20, "normal"))

    if ball.xcor() < -790:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_A, score_B), align = "center", font=("courier", 20, "normal"))

    if ball.ycor() > 690:
        ball.dy *=-1
    if ball.ycor()< -690:
        ball.dy *=-1

#Hacer colisones
    if ((ball.xcor() > 600 and ball.xcor() < 610)
        and (ball.ycor() < playerB.ycor() + 50
        and ball.ycor() > playerB.ycor() - 50 )):
        ball.dx *= -1
        ball.dy += +1
        
    if ((ball.xcor() < -600 and ball.xcor() > -610)
        and (ball.ycor() < playerA.ycor() + 50
        and ball.ycor() > playerA.ycor() - 50 )):
        ball.dx *= -1
        ball.dy *= +1
