import turtle

#####################
#
#Falta completar
#
#

wn = turtle.Screen()
jorge = turtle.Turtle()
jorge.speed(200)
#jorge1 = turtle.Turtle()
jorge.shape('turtle')
#jorge1.shape('turtle')
#angle = 360 / 2

for i in range(12):
    jorge.forward(i)
    jorge.right(0)
#jorge1.left(1)
#jorge1.goto(90, 90)
#jorge1.goto(80, 80)

    #jorge1.right(1)

wn.exitonclick()