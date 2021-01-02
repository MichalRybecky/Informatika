import tkinter
c = tkinter.Canvas(height = 500, width = 400)
c.pack()


def pocet_hlasujucich():
    with open ('spokojnost_pisomka_1.txt', 'r', encoding='utf-8') as file:
        lenght = 0
        yes = 0
        line = file.readline()
        while line:
            if "áno" in line:
                yes += 1
            lenght += 1
            line = file.readline()
        return lenght, yes


def graf(yes, perc_yes, perc_no):
    c.create_rectangle(100, 400, 150, 400 - (yes * 10), fill="green")
    c.create_text(125, 420, text=f"Ano\n{perc_yes}%")
    c.create_rectangle(200, 400, 250, 400 - ((lenght - yes) * 10), fill="red")
    c.create_text(225, 420, text=f"Nie\n{perc_no}%")


def perc(lenght, yes):
    perc_yes = int(yes * 100 / lenght)
    perc_no = int((lenght - yes) * 100 / lenght)
    return perc_yes, perc_no


lenght, yes = pocet_hlasujucich()

perc_yes, perc_no = perc(lenght, yes)

graf(yes, perc_yes, perc_no)

print(f"Pocet hlasujucich: {lenght}")


c.mainloop()
