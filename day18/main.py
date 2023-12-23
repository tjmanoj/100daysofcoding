import turtle
import random
# import colorgram
# colors = colorgram.extract("hirst_painting.jpg", 40)
#
# list_of_colors = []
# for i in colors:
#     list_of_colors.append((i.rgb.r, i.rgb.g, i.rgb.b))
# print(list_of_colors)

colors = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]
bubu = turtle.Turtle()
turtle.colormode(255)

bubu.speed("fastest")
bubu.setheading(220)
bubu.penup()
bubu.forward(350)
print(bubu.pos())
bubu.setheading(0)
for j in range(10):
    for i in range(10):
        bubu.dot(20, random.choice(colors))
        bubu.penup()
        bubu.forward(50)
        bubu.pendown()
        bubu.dot(20)
    if j != 9:
        bubu.penup()
        bubu.setheading(90)
        bubu.forward(50)
        bubu.setheading(180)
        bubu.forward(500)
        bubu.setheading(360)

my_screen = turtle.Screen()
my_screen.exitonclick()