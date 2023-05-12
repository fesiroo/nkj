from tkinter import*
def click():
    nct.configure(bg = "#21ed1a")
def click1():
    wayv.configure(bg = "#a6bf26")
def click2():
    svt.configure(bg = "#b5b2d1")
def click3():
    ae.configure(bg = "#44c3c7")
def click4():
    mx.configure(bg = "#751434")
def destroy():
    txt.destroy()
def des1():
    at.destroy()
root = Tk()
root.title("k-pop fandom color")
root.geometry("500x500")
root["bg"] = "#d5ebb5"
nct = Button(root, bg = "#46a37c", text = "NCT", font = ('Arial', 15), command=click)
nct.place(width= 100, height = 60, x = 30, y = 30)
wayv = Button(root, bg = "#f4ffbf", text = "WAYV", font = ('Arial', 15), command = click1)
wayv.place(width= 100, height = 60, x = 30, y = 100)
svt = Button(root, bg = "#f5abcb", text = "SEVENTEEN", font = ('Arial', 15), command=click2)
svt.place(width=150, height = 60, x = 30, y = 170)
ae = Button(root, bg = "#ce5cd6", text = "AESPA", font = ('Arial', 15), command= click3)
ae.place(width= 100, height = 60, x = 30, y = 240)
mx = Button(root, bg = "#0e0640", text = "MONSTA X", fg = "#fcf7f9", font = ('Arial', 15), command = click4)
mx.place(width= 130, height = 60, x = 30, y = 310)
txt = Button(root, bg ="#c5e6d8", text = "TXT", fg ="#4cba9f", font = ('Arial', 15, 'bold'), command= destroy)
txt.place(width = 100, height=60, x = 50, y = 390)
at = Button(root, bg ="#e3a754", text = "ATEEZ", font = ('Arial', 15, 'bold'), command=des1)
at.place(width=120, height=60, x = 190, y = 390)
nctt = Label(root, bg = "#88f2c6", text = "NCTzen", font = ('Arial', 16), fg = "white", cursor= "dotbox")
nctt.place(width= 150, height = 50, x = 150, y = 35)
ww = Label(root, bg ="#54d68a", text = "WayZenNi", font = ('Arial', 16), fg = "white", cursor = "exchange")
ww.place(width= 200, height = 50, x = 150, y = 105)
ss = Label(root, bg = "#ebf78b", text = "Carat", font = ('Arial', 16), fg = "white", cursor = "fleur")
ss.place(width=100, height = 50, x = 200, y = 175)
aee = Label(root, bg = "#ecbbed", text = "MY", font = ('Arial', 16), fg = "white", cursor = "watch")
aee.place(width= 100, height = 50, x = 150, y = 245)
mxx = Label(root, bg = "#555fa3", text = "Monbebe", font = ('Arial', 16), fg = "white", cursor = "spider")
mxx.place(width=150, height=50, x = 180, y = 315)
root.mainloop()