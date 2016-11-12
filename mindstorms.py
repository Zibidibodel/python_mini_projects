import turtle

window = turtle.Screen()
window.bgcolor('red')

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    # Creating Brad to draw me shapes
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(10)
    for i in range(1,61):
        draw_square(brad)
        brad.right(6)

    window.exitonclick()

def draw_triangle(some_turtle, size):
    for i in range(1, 4):
        some_turtle.forward(size)
        some_turtle.left(120)

def draw_fractal(size, position):
    fractal = turtle.Turtle()
    fractal.hideturtle()
    fractal.speed(100)
    fractal.color('yellow')
    fractal.penup()
    fractal.setx(position[0])
    fractal.sety(position[1])
    fractal.pendown()

    draw_triangle(fractal, size)
    fractal.forward(size)
    draw_triangle(fractal, size)
    fractal.forward(size)
    fractal.left(120)
    fractal.forward(size)
    draw_triangle(fractal, size)
    fractal.forward(size)
    draw_triangle(fractal, size)
    fractal.forward(size)
    fractal.left(120)
    fractal.forward(size)
    draw_triangle(fractal, size)
    fractal.forward(size)
    draw_triangle(fractal, size)

start_position = (- 75, -200)

size = 5
for i in range(1, 7):
    draw_fractal(size, start_position)
    size *= 2

window.exitonclick()