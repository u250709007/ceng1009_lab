# # # for i in range(100):
# # #     print("We like Python's turtles!")
# # import turtle
# # from secrets import token_urlsafe
# #
# # # months = ["January", "February","March","April","May","June","July","August","September","October","November","December"]
# # # for month in months:
# # #     print("One of the months of the year is", month)
# #
# # # numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# # # for number in numbers:
# # #     print(number, "square is", number**2)
# #
# # import turtle
# #
# # t = turtle.Turtle()
# # screen = turtle.Screen()
# #
# # t.penup()
# # t.goto(-200,0)
# # t.pendown()
# #
# # for i in range(3):
# #     t.forward(80)
# #     t.left(120)
# #
# # t.penup()
# # t.goto(-100,0)
# # t.pendown()
# #
# # for i in range(4):
# #     t.forward(80)
# #     t.left(90)
# #
# # t.penup()
# # t.goto(20,0)
# # t.pendown()
# #
# # for i in range(6):
# #     t.forward(50)
# #     t.left(60)
# #
# # t.penup()
# # t.goto(0,-200)
# # t.pendown()
# #
# # for i in range(8):
# #     t.forward(50)
# #     t.left(45)
# #
# # screen.exitonclick()
#
# import turtle
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
#
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
# t.pensize(3)
#
# t.stamp()
# t.penup()
#
# for i in range(12):
#     t.forward(125)
#     t.pendown()
#     t.forward(15)
#     t.penup()
#     t.forward(25)
#     t.stamp()
#     t.backward(165)
#     t.left(30)
#
# screen.exitonclick()