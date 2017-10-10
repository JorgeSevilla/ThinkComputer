import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jorge = turtle.Turtle()
jorge.color("black")
# arrow, blank, circle, classic, square, triangle, turtle.
jorge.shape("classic")

print(list(range(5, 60, 2)))
jorge.up()
for size in range(5, 100, 2):     # start with size = 5 and grow by 2
    jorge.stamp()                # leave an impression on the canvas
    jorge.forward(size)          # move tess along
    jorge.right(24)              # and turn her

jorge.down()
for size in range(5, 100, 2):     # start with size = 5 and grow by 2
    jorge.stamp()                # leave an impression on the canvas
    jorge.forward(size)          # move tess along
    jorge.right(24)              # and turn her

# jorge.penup()
# for size in range(5, 100, 2):     # start with size = 5 and grow by 2
#     jorge.stamp()                # leave an impression on the canvas
#     jorge.forward(size)          # move tess along
#     jorge.right(24)              # and turn her



wn.exitonclick()
