import turtle
from oop_ball import Ball
import random
def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    for i in range(num_balls):
        xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
        ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
        vx.append(random.randint(1, 0.01*canvas_width))
        vy.append(random.randint(1, 0.01*canvas_height))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
color_list = []
xpos = []
ypos = []
vx = []
vy = []
ball_color = []

for x in range(num_balls):
    initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)
all_balls = Ball(xpos, ypos, turtle.speed(1), vx, vy, ball_color, ball_radius)

while (True):
    turtle.clear()
    for i in range(num_balls):
        Ball.draw_circle(all_balls, i)
        Ball.move_circle(all_balls, i, canvas_width, canvas_height)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()