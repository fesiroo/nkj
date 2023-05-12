from tkinter import*
import random
import time
root = Tk()
root.title("мячик")
root.resizable(0,0)
canvas = Canvas(root, width= 500, height= 400)
canvas.pack()
root.update()
class Ball:
    def __init__ (self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        start = [-2, -1, 1, 2]
        random.shuffle(start)
        self.x = start[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250,100, text = "Вы проиграли", font = ('Arial', 30))
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 250, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
    def turn_right(self,event):
        self.x = 2
    def turn_left(self,event):
        self.x = -2
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
class Score:
    def __init__ (self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 20, text = self.score, font =('Arial', 15), fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text = self.score)
paddle = Paddle(canvas, "black")
score = Score(canvas, "purple")
ball = Ball(canvas, paddle, score, "yellow")
while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    root.update_idletasks()
    root.update()
    time.sleep(0.01)





