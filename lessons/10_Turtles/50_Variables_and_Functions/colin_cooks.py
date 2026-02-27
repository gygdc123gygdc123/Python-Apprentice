
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(10)                              # Move tina forward by the forward distance
        tina.left(angle)     


colors = ["blue","red","yellow","green","purple"]

for i in range(100)[::-1]:
    tina.begin_fill()
    draw_polygon(i+3)
    tina.color(colors[i%len(colors)])
    tina.end_fill()

turtle.exitonclick()