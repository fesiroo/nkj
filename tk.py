from tkinter import*
import time
root = Tk()
canvas = Canvas(bg = "grey", width=750, height= 550)
canvas.pack()
# canvas.create_line(0,0, 750,550, width=3)
# canvas.create_line(750, 0, 0,550, width=3)
# canvas.create_rectangle(250,100,345,150, fill = "green", outline = "red", activefill= "grey")
# canvas.create_oval(50,500,150,540, fill = "blue", outline = "purple", activefill="orange")
# canvas.create_polygon(10,150 , 40,100, 70,150, fill="brown", outline="pink", activefill= "white")
canvas.create_polygon(150,20, 220,150, 100,150, fill="green")
canvas.create_polygon(160,50, 220,220, 100,220, fill="green")
canvas.create_polygon(180,100, 220,290, 100,290, fill="green")
a = canvas.create_oval(170,80, 150,100, fill="blue")
b = canvas.create_oval(190,100, 170,120, fill="red")
c = canvas.create_oval(140,180, 170,150, fill= "purple")
e = canvas.create_oval(120,150, 150,120, fill = "brown")
canvas.create_line(123,160, 200,300, fill="yellow", width=4)
canvas.create_line(123,260, 200,150, fill="yellow", width=4)
while True:
    for i in range(10):
        canvas.move(a, 3,-2)
        canvas.update()
        canvas.move(b, 3, -2)
        canvas.update()
        canvas.move(c, 3,-2)
        canvas.update()
        canvas.move(e, 3, -2)
        canvas.update()
        time.sleep(0.05)
        canvas.move(a, -3,2)
        canvas.update()
        canvas.move(b, -3,2)
        canvas.update()
        canvas.move(c, -3,2)
        canvas.update()
        canvas.move(e, -3,2)
        canvas.update()
        time.sleep(0.05)



root.mainloop()