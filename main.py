from turtle import Turtle, Screen

t1 = Turtle()
screen = Screen()


def move_forward():
    t1.forward(10)


def turn_right():
    t1.right(10)


def turn_left():
    t1.left(10)


def move_backward():
    t1.back(10)


def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='c', fun=clear_screen)

screen.exitonclick()
