import tkinter as tk
from tkinter import *
from tkinter.colorchooser import *


poot = tk.Tk()


def color1():
    color = askcolor()


def color2():
    color = askcolor()
    rgb, num = color
    lb.insert(1, rgb)
    lb.insert(2, num)

    print(color)


def hexcolor(rgb):
    lb.insert(1, "%02x%02x%02x" % rgb, "HEXCode above")
    lb.insert(2, rgb, "RGB Number")
    print("#%02x%02x%02x" % rgb)

    return "#%02x%02x%02x" % rgb


def clearlb():
    lb.delete(0, END)


lb = tk.Listbox(poot, height=6, width=20, bd=10)
lb.grid(row=7, column=0)
red = 255
blue = 255
green = 255

sp1 = tk.Spinbox(poot, from_=0, to=255, textvariable="red")
sp2 = tk.Spinbox(poot, from_=0, to=255, textvariable="green")

sp3 = tk.Spinbox(poot, from_=0, to=255, textvariable="blue")

spcolor = hexcolor((red, green, blue))


def convert(event=None):
    red = int(sp1.get())
    green = int(sp2.get())
    blue = int(sp3.get())
    hcolor = hexcolor((red, green, blue))
    text2 = tk.Text(poot, bg=hcolor, width=10, height=10)
    text2.grid(row=3, column=3)


# poot.config(bg=hexcolor((255, 0, 122)))


ffb3 = tk.Button(poot, text="clear list", command=clearlb)
ffb3.grid(row=4, column=0)

ffb4 = tk.Button(text="Select Color SHOW INFO", command=color2)
ffb4.grid(row=5, column=0)

ffb5 = tk.Button(text="HEXCOLOR SHOWS COLOR", command=convert)
ffb5.grid(row=6, column=0)


sp1.grid(row=0, column=3)

sp2.grid(row=1, column=3)

sp3.grid(row=2, column=3)

sp1.bind("<Button-1>", convert)
sp2.bind("<Button-1>", convert)
sp3.bind("<Button-1>", convert)


mainloop()
