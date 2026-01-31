"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(5)
tina.begin_fill()
tina.pendown()
tina.circle(80)
tina.color("red")
tina.end_fill()
tina.penup()
tina.goto(0,-200)
tina.begin_fill()
tina.pendown()
tina.circle(100)
tina.color("pink")
tina.end_fill()
tina.penup()
tina.goto(0,160)
tina.pendown()
tina.begin_fill()
tina.circle(50)
tina.end_fill()
tina.penup()
tina.goto(0,)180
tina.pendown()
tina.begin_fill()
tina.circle(20)
tina.fillcolor("black")
tina.end_fill()
# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!