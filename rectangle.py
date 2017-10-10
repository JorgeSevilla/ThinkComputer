import turtle

wn = turtle.Screen()
jorge = turtle.Turtle()

# jorge.forward(150)           # tell alex to move forward by 150 units
# jorge.left(90)               # turn by 90 degrees
# jorge.forward(75)            # complete the second side of a rectangle
# jorge.left(90)
# jorge.forward(150)
# jorge.left(90)
# jorge.forward(80)
#
# wn.exitonclick()
# for i in range(4):
#     turtle.forward(50)
#     turtle.left(90)
for aColor in["yellow", "red", "purple", "blue"]:
    jorge.color(aColor)
    jorge.forward(100)
    jorge.left(90)

wn.exitonclick()