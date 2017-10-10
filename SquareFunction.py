import turtle

wn = turtle.Screen()
jorge = turtle.Turtle()


def drawSquare(x, y):
    for i in range(4):
        x.forward(y)
        x.left(90)


drawSquare(jorge, 200)
wn.exitonclick()