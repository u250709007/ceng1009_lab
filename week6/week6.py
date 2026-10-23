import turtle
screen = turtle.Screen()
screen.bgcolor("lightgreen")
tess = turtle.Turtle()
#
#
#
# #
#  def drawStar(tess, size):
#      tess.color("hotpink")
#      tess.penup()
#      tess.goto(-150, 0)
#      tess.pendown()
# #
# for i in range(5):
#         drawStar(tess, 100)
#         tess.penup()
#         tess.forward(350)
#         tess.right(144)
#         tess.pendown()
#
#
# screen.exitonclick()

def drawSprite(someturtle, legs, length):
     angle = 360/ legs
     for i in range(legs):
         someturtle.forward(length)
         someturtle.backward(length)
         someturtle.left(angle)

# exersize 6
drawSprite(tess, 15, 120)




screen.exitonclick()