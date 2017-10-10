# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths,
# all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)
import turtle
wn = turtle.Screen()
jorgetrian = turtle.Turtle()
jorgesquare = turtle.Turtle()
jorgehexagon = turtle.Turtle()
jorgeoctagon = turtle.Turtle()
jorgetrian.shape("classic")
jorgesquare.shape("classic")
jorgehexagon.shape("classic")
jorgeoctagon.shape("classic")
#jorgetrian.up()
#jorgesquare.right(90)
# jorgetrian.goto(0, 0)
# jorgesquare.goto(150, 50)
#
# # An equilateral triangle
# for triangle in range(3):
#     jorgetrian.forward(100)
#     jorgetrian.left(120)
#
# # A square
# for square in range(4):
#     jorgesquare.forward(100)
#     jorgesquare.left(90)

# A hexagon (six sides)
# for hexagon in range(6):
#     jorgehexagon.forward(100)
#     jorgehexagon.left(45)
#     jorgehexagon.right(105)
#     jorgehexagon.forward(100)

# An octagon (eight sides)
for octagon in range(8):
    jorgeoctagon.forward(70)
    jorgeoctagon.left(360/8)
    # jorgeoctagon.left(45)
    # jorgeoctagon.right(90)
    # jorgeoctagon.forward(70)

wn.exitonclick()