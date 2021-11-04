#   a115_robot_maze.py
import turtle as trtl
import time

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#initial setup
wn.bgpic("maze1.png")

#maze 1 path 1
for i in range(4):
  for j in range(3):
    turn_left()
  move()
  turn_left()
  move()

#reset/change to maze 2
wn.bgpic("maze2.png")
robot.clear()
robot.goto(startx,starty)

#maze 2 path 1
for i in range(3):
  move()
for i in range(3):
  turn_left()
for i in range(2):
  move()

#reset
robot.clear()
robot.goto(startx,starty)
turn_left()

#maze 2 path 2
for i in range(3):
  turn_left()
for i in range(2):
  for j in range(3):
    move()
  turn_left()
move()

#reset/change to maze 3
wn.bgpic("maze3.png")
robot.clear()
robot.goto(startx,starty)
for i in range(3):
  turn_left()
robot.goto(startx,starty)

#maze 3 path 1
for i in range(4):
  move()
  for j in range(3):
    turn_left()
  move()
  turn_left()

#reset/change to custom maze
wn.bgpic("custommaze.png")
robot.clear()
robot.goto(startx,starty)

#custom maze path 1
for i in range(3):
  turn_left()
for i in range(2):
  turn_left()
  for j in range(2):
    for k in range(2):
      move()
    for k in range(3):
      turn_left()
  turn_left()

wn.mainloop()
