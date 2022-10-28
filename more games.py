import turtle

wn = turtle.Screen()
wn.title ("pong by Luffy")
wn.bgcolor("black")
wn.setup(width=800, height=600 )
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#Ball
balls_b = turtle.Turtle()
balls_b.speed(0)
balls_b.shape('square')
balls_b.color("white")
balls_b.penup()
balls_b.goto(0, 0)
balls_b.dx= 2
balls_b.dy = 2

#function part
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y +=-20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y +=-20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main game loop
while True:
    wn.update()

    balls_b.setx(balls_b.xcor() + balls_b.dx)
    balls_b.sety(balls_b.ycor() + balls_b.dy)