# a123_apple_avalanche - Brianna Adewinmbi and Kyle Huang 
import turtle
import random
import string

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

ground_height = -150
turtle_list = []

for i in range(0, 5):
  new_turtle = turtle.Turtle()
  new_turtle.color("white")
  new_turtle.penup()
  new_turtle.goto(-150 + (i * 75), random.randint(0, 100))
  turtle_list.append(new_turtle)

active_apple = turtle_list[0]
apple_index = 0

alphabet = list(string.ascii_lowercase)

current_letters = []
for i in range(0,5):
  current_letter = alphabet.pop(random.randint(0, len(alphabet)))
  current_letters.append(current_letter)

#-----functions----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple():
  for i in turtle_list:
    i.shape(apple_image)
    wn.update()
    wn.tracer(False)
    i.penup()
    i.speed(0)
    i.goto(i.xcor() - 18, i.ycor() - 40)
    i.write(current_letters[turtle_list.index(i)], font=("Helvetica", 45, "normal"))
    i.goto(i.xcor() + 18, i.ycor() + 40)
    i.speed(1)
    wn.tracer(True)

def drop_apple():
  global apple_index
  global active_apple
  active_apple.clear()
  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.hideturtle()
  apple_index += 1
  if (apple_index < 5):
    active_apple = turtle_list[apple_index]
    wn.onkeypress(drop_apple, current_letters[apple_index])

#-----function calls-----
draw_apple()

wn.onkeypress(drop_apple, current_letters[apple_index])

wn.listen()

wn.mainloop()