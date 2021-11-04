import turtle as trtl
import math

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
   t = trtl.Turtle(shape=s)
   color = turtle_colors[turtle_shapes.index(s)]
   t.speed(0)
   t.pencolor(color)
   t.color(color)
   my_turtles.append(t)

num_turtles = len(turtle_shapes)
i = 0
while (True):
   iterations = math.floor(i/8)
   t = my_turtles[i%6]
   t.penup()
   t.setheading(0)
   t.goto(25*iterations, 50*iterations + math.sqrt(2*((25*iterations)^2)))
   t.pendown()
   for j in range(i%8):
       t.right(45)
       t.forward(50*(iterations+1))
   t.stamp()
   i += 1

wn = trtl.Screen()
wn.mainloop()
