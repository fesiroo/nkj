from tkinter import*
root = Tk()
root.title("basketball")
canvas = Canvas(root, width = 600, height= 500 )
canvas.pack()
canvas.create_rectangle(280,260, 320,600, fill = "gold")
canvas.create_oval(220, 260, 380, 290, outline = "black")
canvas.create_line(220, 275, 280, 350, fill = "red", width = 4)
canvas.create_line(280, 290, 280, 350, fill = "red", width = 4)
canvas.create_line(380, 275, 320, 350, fill = "red", width = 4)
canvas.create_line(320, 290, 320, 350, fill = "red", width = 4)
canvas.create_line(280, 350, 320, 350, fill = "red", width = 4)
canvas.create_line(280, 350, 280, 390, fill = "red", width = 4)
canvas.create_line(320, 350, 320, 390 , fill = "red", width = 4)
ball = canvas.create_oval(150, 450, 200, 500, fill = "orange")
def move_ball(event):
    if event.keysym == 'Up':
        canvas.move(ball, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(ball, 0, 5)
    elif event.keysym == 'Right':
        canvas.move(ball, 5, 0)
    elif event.keysym == 'Left':
        canvas.move(ball, -5, 0)
while True:
    canvas.bind_all('<Down>', move_ball)
    canvas.bind_all('<Up>', move_ball)
    canvas.bind_all('<Right>', move_ball)
    canvas.bind_all('<Left>', move_ball)
    canvas.update()

root.mainloop()