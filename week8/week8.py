# # def get_grade(mark):
# #     if mark >= 90:
# #         return "A"
# #     elif mark >= 80:
# #         return "B"
# #     elif mark >= 70:
# #         return "C"
# #     elif mark >= 60:
# #         return "D"
# #     else:
# #         return "F"
# #
# # marks = [95, 90, 89, 9, 80, 79, 9, 70, 65, 60, 59, 5, 0]
# # for mark in marks:
# #     print("Grade is ", get_grade(mark))
# import turtle
#
#
# def chooseColor(height):
#
#    if height >= 200:
#        return "red"
#    elif height >= 100:
#        return "yellow"
#    else:
#        return "green"
#
# def drawBar (t, height, gap):
#      if height >= 0:
#          lebelY = height + gap
#      else:
#          lebelY = gap
#      t.penup()
#      t.left(90)
#      t.forward(lebelY)
#      t.write("  " + str(height))
#      t.backward(lebelY)
#      t.right(90)
#      t.pendown()
#
#      t.fillcolor(chooseColor(height))
#      t.begin_fill()
#      t.left(90)
#      t.forward(height)
#      t.right(90)
#      t.forward(40)
#      t.right(90)
#      t.forward(height)
#      t.left(90)
#      t.end_fill()
#
#
# def barChart(data):
#     max_height = max(data)
#     min_height = min(data)
#     num_bars = len(data)
#
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#
#     right = 40 * num_bars + gap
#
#     top = max_height + 4 + border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#     for height in data:
#         drawBar(t, height, gap)
#
#     wn.exitonclick()
#
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)

import math

def findHypot(a,b):
    hypot = (a**2 + b**2) ** 0.5
    return hypot

def calcWithMath(a,b):
    hypot = math.sqrt(a**2 + b**2)
    return hypot

print(findHypot(3,4))
print(calcWithMath(3,4))

