import turtle

def pythagoras_tree(recursion_level):
    screen = turtle.Screen()
    screen.setup(400,400)

    TTL = turtle.Turtle()
    TTL.speed(0)
    TTL.color('red')
    TTL.pensize(2)

    TTL.penup()
    TTL.setposition(0,-100)
    TTL.pendown()
    TTL.hideturtle()
    TTL.setheading(90)

    branch_length = 50 
    branch_reduction = 5
    angle = 45
    draw_fractal(TTL, recursion_level, branch_length, branch_reduction, angle)
    screen.exitonclick()


def draw_fractal(TTL : turtle.Turtle, recursion_level, branch_length, branch_reduction, angle):
    if recursion_level == 0:
        TTL.fd(0)
    else:
        branch_length = branch_length - branch_reduction
        TTL.forward(branch_length)
        TTL.left(angle)
        draw_fractal(TTL, recursion_level-1, branch_length, branch_reduction, angle)
        TTL.right(angle * 2)
        draw_fractal(TTL, recursion_level-1, branch_length, branch_reduction, angle)
        TTL.left(angle)
        TTL.backward(branch_length)


def main():
    recursion_level = int(input('Write recursion level: '))
    pythagoras_tree(recursion_level)


if __name__ == "__main__":
    main()