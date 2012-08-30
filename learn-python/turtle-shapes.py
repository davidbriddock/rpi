from turtle import *

# set a shape and colour
shape("circle")
shapesize(5,1,2)
fillcolor("red")
pencolor("darkred")

# move to the start
penup()
goto(0, -100)

# stamp out some shapes
for i in range(72):
   forward(10)
   left(5)
   tilt(7.5)
   stamp()

exitonclick()