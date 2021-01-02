import tkinter

c = tkinter.Canvas(width = 600, height = 300)
c.pack()

def kontrola():
    c.delete('all')
    hlasenie = []
    y = 80
    heslo = entry1.get()

    if len(heslo) < 8:
        kratke = True
    else:
        kratke = False

    male_pis = [x for x in heslo if x.islower()]
    velke_pis = [y for y in heslo if y.isupper()]
    cislo = [z for z in heslo if z.isnumeric()]

    if kratke:
        hlasenie.append('Tvoje heslo je prilis kratke.')

    if not male_pis:
        hlasenie.append('Tvoje heslo neobsahuje male pismeno.')

    if not velke_pis:
        hlasenie.append('Tvoje heslo neobsahuje velke pismeno.')

    if not cislo:
        hlasenie.append('Tvoje heslo neobsahuje cislo.')

    if not hlasenie:
        c.create_text(300, 200, text='Tvoje heslo je bezpecne.')
    else:
        for h in hlasenie:
            c.create_text(300, y, text=h)
            y += 50


label1 = tkinter.Label(text='Zadaj heslo: ')
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text="Skontroluj", command=kontrola)
button1.pack()

c.mainloop()
