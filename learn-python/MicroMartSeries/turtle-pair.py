from turtle import *

# create Tom
tom = Turtle()
tom.shape("turtle")
tom.color("red")
tom.pencolor("red")
tom.penup()

# create Tim
tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tom.pencolor("blue")
tim.penup()

# starting positions
tom.forward(150)
tim.backward(150)

# stomp around
dist = 8
for i in range(30):
   tom.stamp()
   tim.stamp()
   dist += 2
   tom.forward(dist)
   tom.right(24)
   tim.forward(dist)
   tim.right(24)

#tom.write("Tom has finshed")
#tim.write("Tim has finshed")

exitonclick()