import turtle

wn = turtle.Screen()
jorge = turtle.Turtle()


def twosquare(x, y):
    for i in range(4):
        x.forward(y)
        x.left(90)


twosquare(jorge, 25)
jorge.penup()
jorge.goto(100, 100)
jorge.pendown()

twosquare(jorge, 50)
jorge.penup()
jorge.goto(100, 100)
jorge.pendown()
jorge.penup()
jorge.goto(200, 200)
jorge.pendown()
twosquare(jorge, 75)

wn.exitonclick()
