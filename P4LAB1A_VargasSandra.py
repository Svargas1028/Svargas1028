import turtle

# Initialize the window
wn = turtle.Screen()
wn.setup(width=800, height=600)  # Set window size
wn.title("Shapes")  # Window title

# Initialize the turtle for the square
square_turtle = turtle.Turtle()
square_turtle.speed(1)  # Drawing speed for the square
square_turtle.penup()  # Lift the pen
square_turtle.goto(-100, 0)  # Move to a position to draw the square
square_turtle.pendown()  # Put the pen down

# Draw the square
for _ in range(4):  # Repeat 4 times for the 4 sides of the square
    square_turtle.forward(100)  # Move forward 100 units
    square_turtle.right(90)  # Turn 90 degrees to the right

# Initialize the turtle for the triangle
triangle_turtle = turtle.Turtle()
triangle_turtle.speed(1)  # Drawing speed for the triangle
triangle_turtle.penup()  # Lift the pen
triangle_turtle.goto(100, -50)  # Move to a position to draw the triangle
triangle_turtle.pendown()  # Put the pen down

# Draw the triangle
for _ in range(3):  # Repeat 3 times for the 3 sides of the triangle
    triangle_turtle.forward(100)  # Move forward 100 units
    triangle_turtle.left(120)  # Turn 120 degrees to the left

# Close the window when clicked
wn.exitonclick()
