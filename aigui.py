# Importing tkinter module
from tkinter import *
import aispeech
import sys
import os
import random
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def callback1(url):
    query2 = url.replace(" ", "+")
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new(f"https://www.google.com/search?q={query2}")

def music():
    music_dir = 'D:\\Music'
    songs = os.listdir(music_dir)
    randomsongs = random.choice(songs)
    os.startfile(os.path.join(music_dir, randomsongs))

def ai():
    os.system('python aispeech.py')

master = Tk()
master.configure(background="#bec1c4")

# setting geometry of tk window
master.geometry("1920x1080")
icon1 = PhotoImage(file=r"D:\GUI\mic.png")
icon2 = PhotoImage(file=r"D:\GUI\chrome.png")
icon3 = PhotoImage(file=r"D:\GUI\weather1.png")
icon4 = PhotoImage(file=r"D:\GUI\instagram2.png")
icon5 = PhotoImage(file=r"D:\GUI\twitter.png")
icon6 = PhotoImage(file=r"D:\GUI\calculator.png")
icon7 = PhotoImage(file=r"D:\GUI\gallery.png")
icon8 = PhotoImage(file=r"D:\GUI\notepad.png")
icon9 = PhotoImage(file=r"D:\GUI\fb.png")
icon10 = PhotoImage(file=r"D:\GUI\img2.png")
icon11 = PhotoImage(file=r"D:\GUI\searchbar.png")
icon12 = PhotoImage(file=r"D:\GUI\search.png")

photo = PhotoImage(file=r"D:\GUI\finalicon.png")
tmi13 = photo.subsample(1, 1)
master.iconphoto(False, photo)

tmi1 = icon1.subsample(5, 5)
tmi2 = icon2.subsample(7, 7)
tmi3 = icon3.subsample(7, 7)
tmi4 = icon4.subsample(7, 7)
tmi5 = icon5.subsample(7, 7)
tmi6 = icon6.subsample(7, 7)
tmi7 = icon7.subsample(7, 7)
tmi8 = icon8.subsample(7, 7)
tmi9 = icon9.subsample(7, 7)
tmi10 = icon10.subsample(1, 1)
tmi11 = icon11.subsample(1, 1)
tmi12 = icon12.subsample(12, 12)

label = Label(master, image=tmi10, bg="#bec1c4")
label.place(relx=0.5, rely=0.38, anchor=CENTER)

label1 = Label(master, image=tmi11, bg="#bec1c4")
label1.place(relx=0.5, rely=0.645, anchor=CENTER)

f = Entry(master, width=30, borderwidth=0, bg="#353b48", fg="white", font="times 20 italic")
f.grid(row=0, column=0, columnspan=3, padx=530, pady=500)

# label2 = Label(master, image=tmi12, bg="#bec1c4")
# label2.place(relx=0.5, rely=0.4, anchor=CENTER)

b1 = Button(master, cursor="hand2")
b1.config(image=tmi1, width=140, height=140, bd=0, bg="#bec1c4", compound=RIGHT)
b1.bind("<Button-1>", lambda e: ai())
b1.place(relx=0.5, rely=0.825, anchor=CENTER)

b2 = Button(master, cursor="hand2")
b2.config(image=tmi2, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b2.bind("<Button-1>", lambda e: os.startfile("C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"))
b2.place(relx=0.16, rely=0.75, anchor=CENTER)

b3 = Button(master, cursor="hand2")
b3.config(image=tmi3, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b3.bind("<Button-1>", lambda e: callback("https://www.accuweather.com/"))
b3.place(relx=0.83, rely=0.75, anchor=CENTER)

b4 = Button(master, cursor="hand2")
b4.config(image=tmi4, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b4.bind("<Button-1>", lambda e: callback("https://www.instagram.com/"))
b4.place(relx=0.33, rely=0.75, anchor=CENTER)

b5 = Button(master, cursor="hand2")
b5.config(image=tmi5, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b5.bind("<Button-1>", lambda e: callback("https://twitter.com/explore"))
b5.place(relx=0.67, rely=0.75, anchor=CENTER)

b6 = Button(master, cursor="hand2")
b6.config(image=tmi6, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b6.bind("<Button-1>", lambda e: os.system('start Calculator:'))
b6.place(relx=0.16, rely=0.90, anchor=CENTER)

b7 = Button(master, cursor="hand2")
b7.config(image=tmi7, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b7.bind("<Button-1>", lambda e: os.startfile("D:\\Pins"))
b7.place(relx=0.83, rely=0.90, anchor=CENTER)

b8 = Button(master, cursor="hand2")
b8.config(image=tmi8, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b8.bind("<Button-1>", lambda e: os.system('notepad'))
b8.place(relx=0.33, rely=0.90, anchor=CENTER)

b9 = Button(master, cursor="hand2")
b9.config(image=tmi9, width=100, height=100, bd=0, bg="#bec1c4", compound=RIGHT)
b9.bind("<Button-1>", lambda e: callback("https://www.facebook.com/"))
b9.place(relx=0.67, rely=0.90, anchor=CENTER)

b11 = Button(master, cursor="hand2")
b11.config(image=tmi12, width=40, height=40, bd=0, bg="#353b48", compound=RIGHT, command=lambda: callback1(f.get()))
# b11.bind("<Button-1>", lambda: callback(e.get()))
b11.place(relx=0.645, rely=0.645, anchor=CENTER)

h = Label(master, text="\tHello there, I am Nick.", font=('times', 50, 'bold', 'italic'), fg="#2e2e2e")
h.place(relx=0.420, rely=0.10, anchor=CENTER)
h.configure(background="#bec1c4", bd=0, compound=RIGHT)

l1 = Label(master, text="Open Youtube", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic ")
l1.place(x=180, y=470)
l1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/"))
l1.configure(background="#bec1c4")

l2 = Label(master, text="Play Music", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic ")
l2.place(x=1200, y=380)
l2.bind("<Button-1>", lambda e: music())
l2.configure(background="#bec1c4")

l3 = Label(master, text="Open college website", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic")
l3.place(x=180, y=200)
l3.bind("<Button-1>", lambda e: callback("https://www.gndec.ac.in/"))
l3.configure(background="#bec1c4")

l4 = Label(master, text="Open Google", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic")
l4.place(x=180, y=290)
l4.bind("<Button-1>", lambda e: callback("https://www.google.com/"))
l4.configure(background="#bec1c4")

l5 = Label(master, text="Open w3schools", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic")
l5.place(x=180, y=380)
l5.bind("<Button-1>", lambda e: callback("https://www.w3schools.com/"))
l5.configure(background="#bec1c4")

l6 = Label(master, text="Open Gmail", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic")
l6.place(x=1182, y=290)
l6.bind("<Button-1>", lambda e: callback("https://mail.google.com/"))
l6.configure(background="#bec1c4")

l7 = Label(master, text="Open Google Translate", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic")
l7.place(x=1032, y=200)
l7.bind("<Button-1>", lambda e: callback("https://translate.google.co.in/"))
l7.configure(background="#bec1c4")

l8 = Label(master, text="Show daily news", fg="#2e2e2e", cursor="hand2", font="times 25 bold italic")
l8.place(x=1127, y=470)
l8.bind("<Button-1>", lambda e: callback("https://www.indiatoday.in/"))
l8.configure(background="#bec1c4")

mainloop()