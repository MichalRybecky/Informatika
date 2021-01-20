import tkinter
c = tkinter.Canvas(height = 500, width = 600)
c.pack()

"""
Ak by si chcel nevytvarat zbytocne funkcie iba na to, aby ti iba pustili dalsiu funkciu,
vies si importnut partial z functools ako:
`from functools import partial`

a potom vies za command dat partial(funkcia, argument1, argument2...)
`command=partial(tajnicka, True/False)`

Tymto sposobom ti netreba dve zbytocne funkcie ktore skoro nic nerobia
"""

with open("krizovka.txt", "r") as subor:
    krizovka = []
    for riadok in subor:
        krizovka.append(riadok.strip())


def vypln():
    tajnicka(vyplnit=True)

def odvypln():
    tajnicka(vyplnit=False)


button = tkinter.Button(text = "Vyplnit", width = 10, command = vypln)
button.pack()
button2 = tkinter.Button(text = "Odvyplnit", width = 10, command = odvypln)
button2.pack()


def tajnicka(vyplnit):
    y = 100
    # z = 1
    # z je dobry napad na cislovanie riadkov, ale mal by sa pouzivat priamo vo for loope s funkctiou `enumerate`
    # tymto sposobom je jasne, co je z za premennu a nemusis ho zvysovat
    for z, slovo in enumerate(krizovka):
        posun = 50 # pokial posun inde ako v riadku dole nepouzivas, mozes ho vlozit do toho kodu, nemusis ho davat ako premennu, zle to ale nie je
        x = 200 - (posun * int(slovo[0]))
        a = len(slovo) - 2
        # f = "white"
        # nepotrebujes na zaciatku kazdeho loopnutia menit farbu, kedze tam mas `if`, ktory ju urcite zmeni aj tak
        c.create_text(x - 15, y - 25, text = z+1)
        for i in range(a):
            if x == 150:
                f = "gray"
            # if x != 150:
            # uz si sa pytal, ci `x == 150`. Pokial nie je, netreba sa zase pytat, ci sa nerovna,
            # uz bude vzdy ine ako 150, preto ti staci `else`
            else:
                f = "white"
            c.create_rectangle(x, y, x + 50, y - 50, fill = f)
            if vyplnit == True:
                c.create_text(x + 25, y - 25, text = slovo[2 + i])
            x += 50
        y += 50

tajnicka(False)

c.mainloop()
