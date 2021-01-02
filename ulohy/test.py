import tkinter
import random

with open('nahodne_slova.txt', 'r') as file:
    slova = [x.strip() for x in file.readlines()]


def setup():
    global slovo, progress, time_left
    slovo = list(random.choice(slova))
    progress = list(len(slovo) * '*')
    time_left = len(slovo) * 2


def casovac():
    for i, char in enumerate(slovo):
        if key == char:
            progress[i] = key
    if progress == slovo:
        setup()
    print('tik')
    print(key, slovo, progress, time_left)
    c.delete('all')
    c.after(100, casovac)


def key(event):
    global key
    key = event.keysym


c = tkinter.Canvas()
c.pack()
c.bind_all('<Key>', key)

setup()
casovac()

c.mainloop()
