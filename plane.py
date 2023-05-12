import turtle 
import time
t = turtle.Pen()
ts = turtle.Screen()
ts.screensize(250,500)
ts.title("plane")
t.up()
t.goto(250,200)
t.down()
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.color("black")
t.pensize(5)
t.home()
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.goto(-300,150)
t.goto(100,50)
t.goto(0,0)
t.end_fill()
t.goto(-30,-125)
t.goto(-50,-50)
t.begin_fill()
t.goto(-300,150)
t.goto(-125,-125)
t.goto(-50,-50)
t.goto(-30,-125)
t.goto(-85,-85)
t.end_fill()
t.pensize(3)
t.up()
t.goto(75,25)
t.down()
t.goto(200,0)
t.up()
t.goto(50,-5)
t.down()
t.goto(250,-30)
t.up()
t.goto(10,-80)
t.down()
t.goto(100,-150)
t.up()
t.goto(-80,-125)
t.down()
t.goto(120,-200)













time.sleep(10)
