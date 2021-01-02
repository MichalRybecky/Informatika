'''
Vianocna pohladnica
vlocky menia rychlost a smer podla polohy kurzora
'''

import tkinter
from random import randint

c = tkinter.Canvas(width=750, height=500)
c.pack()


def create_vlocky():
    return [[randint(-250, 1000), randint(-500, 0), randint(5, 20)] for _ in range(300)]


def create_additional_vlocka():
    return [randint(-250, 1000), randint(-500, 0), randint(5, 20)]


def mouse(event):
    global x, y
    x = event.x
    y = event.y


c.create_rectangle(0, 0, 750, 500, fill='lightgrey', outline='')
c.create_rectangle(50, 50, 700, 450, fill='red', outline='')
c.create_rectangle(65, 65, 685, 435, fill='lightgrey', outline='')
c.create_text(375, 200, text='Veselé Vianoce', font='arial 50 bold', fill='red')



c.bind('<Motion>', mouse)

positions_x = {
    0.5: 0, 0.4: -1, 0.3: -2, 0.2: -3, 0.1: -4, 0: -5,
    0.6: 1, 0.7: 2, 0.8: 3, 0.9: 4, 1.0: 5
    }
vlocky = create_vlocky()
x, y, a = 0, 0, 0
while True:
    c.delete('t')
    x_pos = round(x / 750, 1)
    y_pos = round(y / 750, 1)
    print(y_pos)
    vlocky.append(create_additional_vlocka())
    vlocky.append(create_additional_vlocka())
    for vlocka in vlocky:
        c.create_text(vlocka[0], vlocka[1], text='*', fill='white', font=f"arial {vlocka[2]}", tag='t', angle=a)
        vlocka[1] += (y_pos) * 10
        vlocka[0] += positions_x[x_pos]
    a += 3
    c.update()
    c.after(20)


c.mainloop()
