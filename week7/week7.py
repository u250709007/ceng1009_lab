# # # # import math
# # # #
# # # # def aySqrt(x):
# # # #     guess = x / 2
# # # #     for i in range(20):
# # # #         guess = x / 2 * (guess + x / guess)
# # # #         print(guess)
# # # #     return guess
# # # #
# # # # n = int(input("Enter a positive integer: "))
# # # # print(aySqrt(n))
# # # # print(math.sqrt(n))
# # #
# # # import turtle
# # # def drawSprite(someturtle, legs, lenght):
# # #     angle = 360 / legs
# # #     for i in range(legs):
# # #         someturtle.forward(lenght)
# # #         someturtle.backward(lenght)
# # #         someturtle.left(angle)
# # #
# # # def fancySquare(t, size):
# # #     for corner in range(4):
# # #         drawSprite(t, 8, 20)
# # #         t.forward(size)
# # #         t.left(90)
# # #
# # # wn = turtle.Screen()
# # # wn.bgcolor("lightgreen")
# # #
# # # t = turtle.Turtle()
# # # t.color("hotpink")
# # # t.pensize(2)
# # #
# # # fancySquare(t, 100)
# # # wn.exitonclick()
# #
# # import turtle
# # def drawTip(t, size):
# #     t.begin_fill()
# #     t.left(90)
# #     t.forward(size/2)
# #     t.right(120)
# #     t.forward(size)
# #     t.right(120)
# #     t.forward(size)
# #     t.right(120)
# #     t.forward(size/2)
# #     t.right(90)
# #     t.end_fill()
# #
# # def drawSpriteWithTips(someturtle, legs, length):
# #     angle = 360/legs
# #     for i in range(legs):
# #         someturtle.forward(length)
# #         drawTip(someturtle, 10)
# #         someturtle.backward(length)
# #         someturtle.left(angle)
# #
# # def fancySquare(t, size):
# #     for corner in range(4):
# #         drawSpriteWithTips(t, 8, 20)
# #         t.forward(size)
# #         t.left(90)
# #
# # wn = turtle.Screen()
# # wn.bgcolor("black")
# #
# # t = turtle.Turtle()
# # t.color("white")
# #
# # t.pensize(2)
# #
# # fancySquare(t, 100)
# #
# # wn.exitonclick()
#
#
# def checkSign(n):
#     if n > 0:
#         return "positive"
#     elif n < 0:
#         return "negative"
#     else:
#         return "zero"
#
# num_list = [-7, 5, 0]
#
# for number in num_list:
#     print(checkSign(number))
#
# n = int(input("Enter a number: "))
# print(checkSign(n))

import turtle

def drawBar(t, height, gap):
    t.penup()
    t.left(90)
    t.forward(height + gap)
    t.write(" " + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)

    border = 10

    gap = (maxheight - border) / 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = maxheight + 4 * border
    wn.setworldcoordinates(-border, -border, right, top)

    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawBar(t, height, gap)

    wn.exitonclick()

data = [48, 117, 200, 240, 160, 260, 220]

barChart(data)