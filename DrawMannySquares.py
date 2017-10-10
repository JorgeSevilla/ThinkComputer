import turtle


def squaredraw(t, sz):
    """Functoin for draw square"""
    for i in range(4):
        t.forward(sz)
        t.right(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

jorge = turtle.Turtle()
jorge.color("hotpink")
jorge.pensize(3)

for i in range(5):
    squaredraw(jorge, 20)  # Call tu fuction for draw more squares
    jorge.penup()
    jorge.forward(40)  # Move jorge to starting position for the next square.
    jorge.pendown()

#squaredraw(jorge, 20)

wn.exitonclick()