# Write a program that asks the user for the number of sides, the length of the side, the color,
# and the fill color of a regular polygon. The program should draw the polygon and then fill it in.

import turtle

wn = turtle.Screen()


numbers = int(input("Please enter a number: "))
color = input("Please enter a color: ")
angle = 360 / numbers
jorge = turtle.Turtle()

for i in range(numbers):
    jorge.color(color)
    jorge.forward(50)
    jorge.left(angle)

wn.exitonclick()  # Close ti click