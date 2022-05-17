#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "square", "triangle", "classic"]
horiz_colors = ["blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo"]
crashed_turtles = []

tloc = 50
for i in range(len(turtle_shapes)):
    s = turtle_shapes[i]

    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors[i]
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors[i]
    vt.fillcolor(new_color)
    vt.goto( -tloc, 350)
    vt.setheading(270)

    tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
steps = 5
while steps < 55:
    for ht in horiz_turtles:
        for vt in vert_turtles:
            speed = ((steps%10)-5)*((steps%10)-5)/3
            if (crashed_turtles.__contains__(ht)):
                ht.forward(max(-speed*4,-30))
                ht.shape(turtle_shapes[horiz_turtles.index(ht)])
                ht.fillcolor(horiz_colors[horiz_turtles.index(ht)])
                crashed_turtles.remove(ht)
            if (crashed_turtles.__contains__(vt)):
                vt.forward(max(-speed*6,-45))
                vt.shape(turtle_shapes[vert_turtles.index(vt)])
                vt.fillcolor(vert_colors[vert_turtles.index(vt)])
                crashed_turtles.remove(vt)
            if (ht.xcor() <= 200):
                ht.forward(speed)
            if (vt.ycor() >= -200):
                vt.forward(speed)
            if (abs(ht.xcor()-vt.xcor()) <= 20 and abs(ht.ycor()-vt.ycor()) <= 20):
                ht.shape("circle")
                ht.fillcolor("red")
                vt.shape("circle")
                vt.fillcolor("red")
                crashed_turtles.append(ht)
                crashed_turtles.append(vt)
    steps = steps + 1
# End of program notifier
for i in range(len(horiz_turtles)):
    horiz_turtles[i].color("gray")
    vert_turtles[i].color("gray")
wn = trtl.Screen()
wn.mainloop()

