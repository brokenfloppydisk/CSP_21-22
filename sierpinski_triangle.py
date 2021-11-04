# Sierpinski's Triangle program - Kyle Huang
# Period 5 CSP - 10/11/21

# Import statements
import turtle as trtl
import math
import random

# Initialize window and set color mode to 8-bit color
wn = trtl.Screen()
wn.colormode(255)

# Initialize turtle
triangle = trtl.Turtle()
triangle.shape("triangle")
triangle.speed(0)
triangle.hideturtle()

# The number of iterations
iterations = 10

# The side length of the zeroth-iteration triangle
side_length = 200

# The top left corner of each triangle in the serpinski's triangle
triangle_points = [(-side_length/2, 0)]

# Function definitions -------------------------------------------

def calculate_triangle_height(triangle_side_length):
    """Calculate the height of an equilateral triangle given the side length.

    Keyword arguments:
    triangle_side_length -- the side length of the triangle
    """
    return math.sqrt((3/4) * side_length * side_length)

def draw_triangle(side_length, x_coord, y_coord, upwards = False, fill = True):
    """Draw an equilateral triangle.

    Keyword arguments:
    side_length -- the side length
    x_coord -- the x coordinate of the left corner of the triangle
    y_coord -- the y coordinate of the left corner of the triangle
    upwards -- whether the triangle should point upwards or downwards (default False)
    fill -- whether the triangle should be filled in (default True)
    """
    triangle.setheading(0)
    triangle.penup()
    triangle.goto(x_coord,y_coord)
    triangle.pendown()
    if (fill):
        triangle.begin_fill()
    for i in range(3):
        triangle.forward(side_length)
        triangle.right(-120 if upwards else 120)
    if (fill):
        triangle.end_fill()

def divide_triangle_points():
    """Divides the triangle points into the next 3 triangle points.
    """
    new_triangle_points = []
    for i in triangle_points:
        triangle_height = calculate_triangle_height(side_length)
        new_triangle_points.append((i[0]-side_length/2, i[1] - triangle_height))
        new_triangle_points.append((i[0]+side_length*3/2, i[1] - triangle_height))
        new_triangle_points.append((i[0]+side_length/2, i[1] + triangle_height))
    return new_triangle_points

# Body -----------------------------------------------------------

#Draw initial triangle
draw_triangle(side_length*2, -side_length, -calculate_triangle_height(side_length), True, False)

# Draw the Serpinski's Triangle
for i in range(iterations):
    # Set color to a random color
    triangle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    # Draw a triangle at each point
    for j in triangle_points:
        draw_triangle(side_length, j[0], j[1], False, True)
    
    # Prepare for next iteration
    side_length = side_length/2
    triangle_points = divide_triangle_points()

# Stop window from closing after completion
wn.mainloop()