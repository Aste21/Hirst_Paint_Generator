import colorgram
import turtle
import random

colors = colorgram.extract("image.jpg", 10)
rgb_colors = []

for color in colors:
    new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    if new_color[0] + new_color[1] + new_color[2] < 240 * 3:
        rgb_colors.append(new_color)

print(rgb_colors)


turtle.colormode(255)
tim = turtle.Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.penup()
screen = turtle.Screen()
color_list = [(40, 7, 178), (87, 248, 180), (219, 156, 111), (146, 6, 81),
              (239, 45, 119), (11, 211, 85)]

tim.sety(-250)
tim.setx(-250)

for x in range(10):
    for i in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)
    tim.sety(-250 + (x + 1) * 50)
    tim.setx(-250)

screen.exitonclick()
