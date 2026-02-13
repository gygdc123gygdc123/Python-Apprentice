
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()        

def make_shape(sides, side_length):
    angle = 360/sides
    for i in range(sides):
        tina.forward(side_length)
        tina.left(angle)
              # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 
tina.begin_fill()
tina.left(90)
tina.circle(100,180)
tina.forward(150)
tina.circle(100,180)
tina.forward(150)
tina.end_fill()
tina.goto(-20,-120)
tina.begin_fill()
tina.circle(80)
tina.color("white")
tina.end_fill()

tina.penup()
tina.goto(-90, 20)
tina.pendown()
tina.begin_fill()
tina.left(90)
make_shape(3,20)
tina.color("orange")
tina.end_fill()
tina.fillcolor()
tina.penup()
tina.goto(-130,70)
tina.pendown()
tina.color("white")
tina.begin_fill()
tina.circle(20)
tina.color("white")
tina.end_fill()
tina.penup()
tina.goto(-130,60)
tina.pendown()
tina.begin_fill()
tina.circle(10)
tina.color("black")
tina.end_fill()
tina.penup()
tina.goto(-70,70)
tina.pendown()
tina.color("white")
tina.begin_fill()
tina.circle(20)
tina.color("white")
tina.end_fill()
tina.penup()
tina.goto(-70,60)
tina.pendown()
tina.begin_fill()
tina.circle(10)
tina.color("black")
tina.end_fill()
turtle.exitonclick()          