# a121_catch_a_turtle.py
# Kyle Huang - CSP Period 5
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_size = 2
spot_shape = "circle"
spot_color = "pink"

score = 0
timer = 30
counter_interval = 1000
timer_up = False

font_setup = ("Helvetica", 20, "normal")

shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

spot_shrink_factor = 0.95

game_width = 400
game_height = 300

wn = trtl.Screen()
wn.colormode(255)

#-----initialize turtle-----
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-10, game_height/2 + 10)

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-60, game_height/2 + 50)

spot = trtl.Turtle(shape=spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def create_background(border_color, border_fill_color):
    border_drawer = trtl.Turtle()
    border_drawer.fillcolor(border_fill_color)
    border_drawer.pencolor(border_color)
    border_drawer.speed(0)
    border_drawer.hideturtle()
    border_drawer.penup()
    border_drawer.goto(-game_width/2, game_height/2)
    border_drawer.setheading(0)
    border_drawer.pendown()
    border_drawer.begin_fill()
    for i in range(2):
        border_drawer.forward(game_width)
        border_drawer.right(90)
        border_drawer.forward(game_height)
        border_drawer.right(90)
    border_drawer.penup()
    border_drawer.end_fill()

    for i in range(200):
        x = rand.randint(-game_width/2 + 20, game_width/2 - 20)
        y = rand.randint(-game_height/2 + 20, game_height/2 - 20)
        color = [rand.randint(0,255),rand.randint(0,255), rand.randint(0,255)]
        border_drawer.color(color[0],color[1],color[2])
        border_drawer.shape(rand.choice(shapes))
        border_drawer.setheading(rand.randint(0,365))
        border_drawer.goto(x,y)
        border_drawer.stamp()

def spot_clicked(x, y):
    change_position()
    update_score()

def change_position():
    spot.penup()
    spot.hideturtle()
    speed = spot.speed()
    spot.speed(0)
    new_xpos = rand.randint((-game_width/2) + (20*spot_size), (game_width/2) - (20*spot_size))
    new_ypos = rand.randint((-game_height/2) + (20*spot_size), (game_height/2) - (20*spot_size))
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()
    spot.pendown()
    spot.speed(speed)
    if (spot.shapesize()[0] >= (0.5/spot_shrink_factor)):
        spot.shapesize(spot.shapesize()[0]*spot_shrink_factor)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        spot.hideturtle()
        spot.penup()
        spot.goto(0,-10*game_height)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

#-----events----------------
create_background("black","gray")

spot.onclick(spot_clicked)

wn.ontimer(countdown, counter_interval)
wn.mainloop()