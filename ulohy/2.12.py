import tkinter

c = tkinter.Canvas(width = 750, height = 750)
c.pack()

with open('noty.txt', 'r') as file:
    noty = [x.strip() for x in file.readline()]
noty.pop()


def ciary(y):
    for _ in range(5):
        c.create_line(0, y, 750, y)
        y += 20


ciary(200)
x = 50
odsadenie = 200
opt = {'c': 100, 'd': 90, 'e': 80, 'f': 70, 'g': 60, 'a': 50, 'h': 40}

for nota in noty:
    y = odsadenie + opt[nota]
    if x > 700:
        x = 50
        odsadenie += 200
        y += 200
        ciary(odsadenie)
    c.create_oval(x - 7, y - 5, x + 7, y + 5)
    x += 35

c.mainloop()
