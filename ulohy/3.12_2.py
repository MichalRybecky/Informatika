import tkinter
import random
import sys

c = tkinter.Canvas(width = 750, height = 500)
c.pack()

with open('nahodne_slova.txt', 'r') as file:
    slova = [x.strip() for x in file.readlines()]


def setup(body):
    slovo = list(random.choice(slova))
    progress = list(len(slovo) * '*')
    time_left = float(len(slovo) * 2)
    hra(slovo, progress, time_left, body)


def hra(slovo, progress, time_left, body):
    if progress == slovo:
        body += 1
        uhadol(body, slovo)
    elif time_left <= 0:
        prehral(body)
    else:
        c.delete('t')
        print(slovo, progress, time_left)
        c.create_text(375, 300, text=progress, font='arial 70 bold', tag='t')
        c.create_text(700, 50, text=body, font='arial 40 bold', tag='t')
        if time_left % 1 == 0:
            c.delete('p')
            c.create_text(50, 50, text=int(time_left), font='arial 40 bold', tag='p')
        for i, char in enumerate(slovo):
            if key == char:
                progress[i] = key
        time_left = round((time_left - 0.01), 2)
        c.update()
        c.after(10, hra, slovo, progress, time_left, body)


def key(event):
    global key
    key = event.char


def prehral(body):
    c.delete('all')
    c.create_text(375, 250, text='Neuhadol si!', font='arial 45', fill='red')
    c.create_text(375, 320, text=f'Pocet bodov: {body}', font='arial 30')
    c.update()
    c.after(2000)
    sys.exit()


def uhadol(body, slovo):
    c.delete('t')
    c.create_text(375, 150, text='Uhadol si!', font='arial 30', fill='green', tag='t')
    c.create_text(375, 300, text=slovo, font='arial 70 bold', tag='t')
    c.create_text(700, 50, text=body, font='arial 40 bold', tag='t')
    c.update()
    c.after(1000)
    setup(body)


body = 0
setup(body)

c.bind_all('<Key>', key)
c.mainloop()
