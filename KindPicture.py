import turtle

wn = turtle.Screen()
jorge = turtle.Turtle()
jorge.hideturtle()
jorge.speed(200)


for i in range(350):
    jorge.color('yellow')
    jorge.forward(i)
    jorge.right(98)

wn.exitonclick()
