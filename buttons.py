from tkinter import*
def click():
    btn.configure(bg = "black")
    root["bg"] = "green"
def click2():
    btn1.configure(bg = "red")
    root["bg"] = "blue"
def destroy():
    btn.destroy()
root = Tk()
root.title("кнопка")
root.geometry("500x500")
root["bg"]="brown"
btn = Button(root,bg = "white", text = "нажми на меня", font = ('Arial', 15, 'bold'), command=destroy)
btn.pack(expand = True, fill = Y, side = RIGHT)
btn1 = Button(root, bg = "pink", text = "press the button", font = ('Arial', 15, 'bold'),command = click2)
# btn1.pack(expand = True, fill = X, side = LEFT)
btn1.place(width = 250, height = 55, x = -10, y = 20)
lbl = Label(root, bg = "orange", text = "eternally", font = ('Arial', 24), fg = "green", justify = RIGHT, cursor= "circle")
lbl.pack(expand = False, fill = X, side = LEFT)
lbl1 = Label(root, bg = "purple", text = "mirror", font = ('Arial', 26, 'bold'), fg = "pink", justify = LEFT, cursor = "heart")
lbl1.pack(expand = False, fill = Y, side = RIGHT)
root.mainloop()
