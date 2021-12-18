from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()
root.title("walmart edition pokemon")
root.geometry("600x400")

root.configure(background="yellow2")

abra=ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulb=ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
button=ImageTk.PhotoImage(Image.open ("button.jpg"))
char=ImageTk.PhotoImage(Image.open ("charmender.jpg"))
ivy=ImageTk.PhotoImage(Image.open ("iyvasour.jpg"))
jig=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kad=ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
nid=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open ("paras.jpg"))
per=ImageTk.PhotoImage(Image.open ("persion.jpg"))
pika=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
rat=ImageTk.PhotoImage(Image.open ("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open ("squirtle.jpg"))

bigglist = [abra,bulb,char,ivy,jig,kad,meowth,nid,paras,per,pika,rat,squirtle]
biggerlist= [30,60,50,100,70,70,60,90,40,70,200,40,50]
p1s=0
p2s=0

def p1():
    global p1s
    rann = random.randint(0,12)
    p1si = bigglist[rann]
    p1sp = biggerlist[rann]
    p1s = p1s + p1sp
    rdl['image'] = p1si
    player1_score['text'] = str(p1s)
    
def p2():
    global p2s
    rann2 = random.randint(0,12)
    p2si = bigglist[rann2]
    p2sp = biggerlist[rann2]
    p2s = p2s + p2sp
    rdl['image'] = p2si
    player2_score['text'] = str(p2s)

player1 = Label(root, text="Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely=0.3, anchor = CENTER)

player2 = Label(root, text="Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely=0.3, anchor = CENTER)

player1_score = Label(root, bg = "royal blue", fg = "white")
player1_score.place(relx = 0.1, rely=0.4, anchor = CENTER)

player2_score = Label(root, bg = "royal blue", fg = "white")
player2_score.place(relx = 0.9, rely=0.4, anchor = CENTER)

rdl = Label(root,bg="chocolate1", fg = "white")
rdl.place(relx=0.5,rely=0.5,anchor=CENTER)

p1button = Button(root, image=button, command = p1)
p1button.place(relx=0.1, rely=0.6, anchor=CENTER)

p2button = Button(root, image=button, command = p2)
p2button.place(relx=0.9, rely=0.6, anchor=CENTER)

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school