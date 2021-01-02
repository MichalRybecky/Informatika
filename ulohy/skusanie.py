import tkinter
import random
import time

c = tkinter.Canvas(width = 750, height = 500)
c.pack()

with open('nahodne_slova.txt', 'r') as file:
    slova = [x.strip() for x in file.readlines()]

def key(event):
    global key
    key = event.char
    print(key)

c.bind_all('<Key>', key)
c.mainloop()
