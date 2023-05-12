from tkinter import*
import time
def move_ball(event):
    if event.keysym == 'Up':
        canvas.move(ball, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(ball, 0, 5)
    elif event.keysym == 'Right':
        canvas.move(ball, 5, 0)
    elif event.keysym == 'Left':
        canvas.move(ball, -5, 0)
root = Tk()
canvas = Canvas(root, width=1000, height=500, bg = "black")
canvas.pack()
ball = canvas.create_oval(20,20, 120,120, fill="white")
canvas.create_text(500, 250, text="txt", fill="black", font = ('Arial, 50'))
for i in range(80):
    canvas.bind_all('<Down>', move_ball)
    canvas.bind_all('<Up>', move_ball)
    canvas.bind_all('<Right>', move_ball)
    canvas.bind_all('<Left>', move_ball)
    canvas.update()
    time.sleep(0.05)
    


root.mainloop()
