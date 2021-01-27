import tkinter
import random

c = tkinter.Canvas(height=500, width=500)
c.pack()


def nakresli(kod, x, y):
    c.create_text(x + 60, y + 115, text=kod)
    for cislo in kod:
        if cislo != '0':
            c.create_rectangle(x, y, x + int(cislo), y + 100, fill="black")
        x += 11  # v zdani je 10px, ale to je prilis male, 1px medzery sa potom nezobrazuju


def key_press(event):
    global pos
    if event.char == " ":
        c.delete("all")
        x, y = 20, 20
        for i, kod in enumerate(kody[pos]):
            if i == 0:
                nakresli(kod, x, y)
                x += 250
            elif i == 2:
                y += 250
                x = 20
                nakresli(kod, x, y)
                x += 250
            else:
                nakresli(kod, x, y)
        pos += 1


with open("ciarovy_kod.txt", "r") as file:
    kody = [x.strip() for x in file.readlines()]
    kody = [kody[x : x + 4] for x in range(0, len(kody), 4)]

pos = 0
nahodny_kod = "".join(["5", str(random.randrange(100000000000, 999999999999))])
print(nahodny_kod)

nakresli(nahodny_kod, 20, 20)

c.bind_all("<Key>", key_press)
c.mainloop()
