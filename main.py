import turtle
import random
import time

# Create screen and modify
screen = turtle.Screen()
screen.title("Clicker Game")
screen.bgcolor("light blue")
screen.setup(width=700, height=650)

# Score and Time Variables
score = 0
timer = 30

# Score Board
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-250, 250)
score_board.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# Timer
timer_board = turtle.Turtle()
timer_board.hideturtle()
timer_board.penup()
timer_board.goto(200, 250)
timer_board.write(f"Time: {timer}", align="left", font=("Arial", 16, "normal"))

clicker_turtle = turtle.Turtle()
clicker_turtle.shape("turtle")
clicker_turtle.color("green")
clicker_turtle.penup()
clicker_turtle.speed(0)

# Score Update Function
def score_update():
    global score
    score += 1
    score_board.clear()
    score_board.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# Timer Update Function
def timer_update():
    global timer
    timer -= 1
    timer_board.clear()
    timer_board.write(f"Time: {timer}", align="left", font=("Arial", 16, "normal"))

# Turtle location update random
def location_update():
    x = random.randint(-250, 250)
    y = random.randint(-200, 200)
    clicker_turtle.goto(x, y)

# Click
def click(x, y):
    if timer > 0:
        score_update()
        location_update()

# Listen click
clicker_turtle.onclick(click)

while timer > 0:
    location_update()
    time.sleep(1)
    timer_update()

# Game Over
timer_board.clear()
timer_board.write("Game Over!", align="left", font=("Arial", 16, "normal"))
clicker_turtle.hideturtle()

# Close screen
screen.mainloop()