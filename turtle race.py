from turtle import Turtle, Screen, penup

t1 = Turtle('turtle')
t1.penup()
t1.goto(-240, 150)
t2 = Turtle('turtle')
t2.penup()
t2.goto(-240, 90)
t3 = Turtle('turtle')
t3.penup()
t3.goto(-240, 30)
t4 = Turtle('turtle')
t4.penup()
t4.goto(-240, -30 )
t5 = Turtle('turtle')
t5.penup()
t5.goto(-240, -90)
t6 = Turtle('turtle')
t6.penup()
t6.goto(-240, -150)
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Bet', 'Which color do you want to bet?: ')




screen.exitonclick()
