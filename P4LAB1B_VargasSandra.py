import turtle

# Initialize the window
wn = turtle.Screen()
wn.title("Initials")  
wn.bgcolor("black")  

# Initialize the turtle
t = turtle.Turtle()
t.speed(2)  
t.pensize(3)  
t.color("purple")  

# Draw the first semicircle (top part of the S)
t.penup()
t.goto(-50, 0)  
t.pendown()
t.circle(50, -180)  

# Draw the second semicircle (bottom part of the S)
t.penup()
t.goto(-50, -0)  
t.pendown()
t.circle(50, -180)  

# Move the turtle to the starting point
t.penup()
t.goto(0, 0)  
t.pendown()

# Draw the letter V
t.goto(-100, 100)  
t.goto(0, 0)  
t.goto(100, 100)  

# Close the window when clicked
wn.exitonclick()
