from turtle import *

pensize(5)

for i in range(4):
   for c in ["red","green","blue"]:
      pencolor(c)
      circle(100)
      right(30)

exitonclick()