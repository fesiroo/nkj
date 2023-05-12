# import turtle
# import time
# t = turtle.Pen()
# ts = turtle.Screen()
# ts.screensize(250,200)
# ts.bgcolor("black")
# t.hideturtle()


# #t.forward(100)
# #t.shape("turtle")
# #t.color("#79f28d")
# #t.pensize(2)
# #t.forward(100)
# #t.color("#fbff00")
# #t.pensize(5)
# #t.left(45)
# #t.forward(100)
# #t.color("#f00")
# #t.pensize(1)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)


# t.fillcolor("yellow")
# t.begin_fill()
# for i in range(36):
#     t.circle(100)
#     t.left(50)
# t.end_fill()

# col = ["blue", "white", "pink", "red"]
# # for i in range(100):
# #     t.pencolor(col[i%4])
# #     t.circle(i)
# #     t.left(91)

# name = turtle.textinput("name", "Write your name")
# for i in range(100):
#     t.pencolor(col[i%4])
#     t.up()
#     t.forward(i*4)
#     t.down()
#     t.write(name, font =( 'Arial', int((i+4)/4)))
#     t.left(91)
    


import turtle
import time
t = turtle.Pen()
ts = turtle.Screen()
ts.bgcolor("black")
t.hideturtle()
t.color("green")
a = 0
while a < 200:
    t.right(a)
    t.forward(a*3)
    a+=1





time.sleep(5)

