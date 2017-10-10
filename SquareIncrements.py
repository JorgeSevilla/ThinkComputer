import turtle


def drawsquare(t, sz):  # Draw square
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

jorge = turtle.Turtle()
jorge.color("hotpink")
jorge.pensize(3)

mv = -10
for i in range(20, 101, 20):  # range for coordinates
    drawsquare(jorge, i)
    jorge.penup()
    jorge.goto(mv, mv)
    jorge.pendown()
    mv = mv - 10

wn.exitonclick()