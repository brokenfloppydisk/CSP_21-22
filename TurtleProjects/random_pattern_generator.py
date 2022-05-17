# CSP Activity 1.1.9 - Algorithms and Art - Kyle Huang - Period 5 - 9/29/21
import turtle as trtl
import random

# Initialize turtle and set speed to instant
turtle = trtl.Turtle()
turtle.speed(0)

# Set window color mode to 255 (so rgb ranges from 0-255)
wn = trtl.Screen()
wn.colormode(255)

def circular_pattern(radius, amount, shape_side_length, shape_sides, shape_offset = 0, shape_color = [0, 0, 0], shape_extent = 360, fill = True):
    """Draws a circular pattern made up of shapes
    
    Keyword arguments:
    radius -- radius of the entire circular pattern
    amount -- number of shapes in the pattern
    shape_side_length -- side length of each shape
    shape_sides -- number of sides on each shape (use 0 for circles)
    shape_offset -- the angle offset of the first shape in degrees (default 0)
    shape_color -- the color of the shapes (default [0, 0, 0])
    shape_extent -- the extent to draw the shapes (default 360)
    fill -- whether or not the shapes should be filled (default True)
    """
    # Loops once for each shape
    for i in range(amount):
        # Go to the origin and turn to the shape's angle
        turtle.penup()
        turtle.goto(0,0)
        turtle.setheading(shape_offset + i*360/amount)

        # Move forward to radius
        turtle.forward(radius)

        # Set pen/fill color (either as a string or as 3 ints)
        if (type(shape_color) == str):
            turtle.color(shape_color)
        else:
            turtle.color(shape_color[0],shape_color[1],shape_color[2])
        turtle.pendown()
        
        # Only fill if fill=True
        if (fill):
            turtle.begin_fill()
        
        # Draw the shape (circle if shape_sides = 0)
        if (shape_sides != 0):
            turtle.circle(shape_side_length, shape_extent, shape_sides)
        else:
            turtle.circle(shape_side_length, shape_extent)
        
        # End fill (if necessary)
        if (fill):
            turtle.end_fill()


def draw_square(side_length, color = [255, 255, 255], fill = True):
    """Draws a square centered at (0,0)
    
    Keyword arguments:
    side_length -- side length of the square
    color -- color of the square (default [255, 255, 255])
    fill -- whether or not the square should be filled in (default True)
    """
    # Set pen/fill color (either as a string or as 3 ints)
    turtle.penup()
    if (type(color) == str):
        turtle.color(color)
    else:
        turtle.color(color[0], color[1], color[2])
    
    # Move turtle to top left of square and turn East
    turtle.goto(-side_length/2,side_length/2)
    turtle.setheading(0)

    # Start fill if necessary
    if (fill):
        turtle.begin_fill()
    
    # Draw the 4 sides
    turtle.pendown()
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    
    # End fill if necessary
    if (fill):
        turtle.end_fill()

# Generate random list of square side lengths
squares = []
for i in range(random.randint(5,20)):
    squares.append(random.randint(10,750))

# Create background square
draw_square(10000, [random.randint(0,255),random.randint(0,255),random.randint(0,255)])

# Sort side lengths from greatest to least
squares.sort(reverse=True)

# Draw squares with random colors
for i in squares:
    color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    draw_square(i, color)

# Generate a random amount of random circular patterns
for i in range(random.randint(10,50)):
    # Generate pattern attributes
    radius = random.randint(10,300)
    amount = random.randint(2,50)
    shape_side_length = random.randint(10,100)
    shape_sides = random.randint(0,8)
    shape_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    shape_extent = random.randint(30,360) * int(random.choice([-1,1]))
    shape_offset = random.randint(0,360)
    fill = bool(random.randint(0,1))

    # Draw pattern
    circular_pattern(radius, amount, shape_side_length, shape_sides, shape_offset, shape_color, shape_extent, fill)

# Make screen persist after program is finished
wn.mainloop()    