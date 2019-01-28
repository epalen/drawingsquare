import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("purple")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    
    #Create the turtle angie - Draws a cirlcle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("red", "yellow")
    #angie.circle(100)
    
    window.exitonclick()
    
draw_art()
