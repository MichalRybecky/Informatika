import tkinter

WIDTH = 1200
c = tkinter.Canvas(width=WIDTH, height=500)
c.pack()

# vyplnit/nevyplnit povodnu tajnicku
VYPLNIT = False
# vedla nevyplnenej krizovky nakresli vyplnenu
KRESLI_VYPLNENU = True
# velkost stvorcekov a pisma
VEL = 20

with open('krizovka.txt', 'r') as file:
    krizovka = [x.strip().split() for x in file.readlines()]


def kresli(pos, slovo, y, posun):
    x = posun - (int(pos) * (VEL * 2))
    for i, s in enumerate(slovo):
        color = ''
        if i + 1 == int(pos):
            color = 'grey'
        c.create_rectangle(x-VEL, y-VEL, x+VEL, y+VEL, fill=color)
        if VYPLNIT:
            vypln(x, y, s)
        x += (VEL * 2)


def vypln(x, y, pismeno):
    c.create_text(x, y, text=pismeno, font=f'arial {VEL}')


# posun znaci posunutie celej tajnicky dolava/do stredu podla toho,
# ci vedla nej ideme kreslit este jednu alebo nie
posun = WIDTH // 4
if not KRESLI_VYPLNENU:
    posun = WIDTH // 2
y = VEL * 2
for slovo in krizovka:
    kresli(slovo[0], slovo[1], y, posun)
    y += VEL * 2

if KRESLI_VYPLNENU:
    y = VEL * 2
    VYPLNIT = True
    posun = WIDTH // 4 * 3
    for slovo in krizovka:
        kresli(slovo[0], slovo[1], y, posun)
        y += VEL * 2


c.mainloop()


