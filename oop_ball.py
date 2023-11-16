import random
import turtle


class Ball:
    def __init__(self, xpos, ypos, speed, vx, vy, color, size):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size

    def draw_circle(self, i):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color[i])
        turtle.fillcolor(self.color[i])
        turtle.goto(self.xpos[i], self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self, i, canvas_width, canvas_height):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (canvas_width - self.size):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (canvas_height - self.size):
            self.vy[i] = -self.vy[i]