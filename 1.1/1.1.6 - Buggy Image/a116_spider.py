#   a116_spider.py
import turtle as trtl

spider = trtl.Turtle()
spider.speed(0)

# create legs
num_legs = 8
leg_length = 50
angle = 75 / (num_legs / 2)
spider.pensize(5)
legs_drawn = 0
while (legs_drawn < num_legs/2):
    for i in [1,-1]:
        spider.penup()
        spider.goto(0,40)
        spider.setheading(i * angle * legs_drawn)
        if (i == 1):
            spider.left(90)
        else:
            spider.right(90)
        spider.pendown()
        spider.circle(leg_length, 120 * i)
    legs_drawn = legs_drawn + 1

# create spider head
spider.penup()
spider.goto(0,0)
spider.setheading(0)
spider.pendown()
spider.pensize(40)
spider.circle(5)
 
# and body
spider.penup()
spider.goto(0, 30)
spider.color("black")
spider.pendown()
spider.pensize(40)
spider.circle(20)
spider.setheading(270)
spider.color("black")
spider.penup()

# create eyes
spider.setheading(-90)
spider.pencolor("purple")
spider.fillcolor("purple")
spider.pensize(1)
for i in [1,-1]:
    spider.goto(10*i, -10)
    spider.begin_fill()
    spider.pendown()
    spider.circle(3)
    spider.end_fill()
    spider.penup()

spider.hideturtle()
 
wn = trtl.Screen()
wn.mainloop()
