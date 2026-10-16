# # # # import math
# # # # a = int(input("enter a: "))
# # # # b = int(input("enter b: "))
# # # #
# # # # c = math.hypot(a, b)
# # # #
# # # # print(c)
# # #
# # # import math
# # #
# # # def areaofcircle(r):
# # #     area = math.pi * r**2
# # #     return area
# # #
# # # print(areaofcircle(5))
# #
# # import turtle
# # def drawstar(t, side):
# #     for i in range(5):
# #         t.forward(side)
# #         t.right(144)
# #
# # tess = turtle.Turtle()
# # screen = turtle.Screen()
# # drawstar(tess, 100)
# # screen.exitonclick()
#
# import turtle
#
# def drawsquare(t, side):
#     for i in range(4):
#         t.fd(side)
#         t.lt(90)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
#
# for i in range(5):
#     drawsquare(tess, 20)
#     tess.penup()
#     tess.forward(50)
#     tess.pendo


def drawsquare(t, side):
    for i in range(4):
        t.fd(side)
        t.lt(90)

import turtle
tess = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("blue")
tess.color("purple")
tess.pensize(3)

for i in range(20, 120, 20):
    drawsquare(tess, i)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()



screen.exitonclick()