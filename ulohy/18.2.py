import tkinter

c = tkinter.Canvas(height=1000, width=2000)
c.pack()


def read_file() -> list:
    # Otvaranie suboru a vytvaranie data listu
    with open("cyklotrasa1.txt", "r") as file:
        data = [x.strip().split(";") for x in file.readlines()]
    data = [[x[0], int(x[1]), float(x[2])] for x in data]
    return data


def write_file():
    # Zapisovanie do dalsieho filu s upravenymi hodnotami
    with open("cyklotrasa2.txt", "w") as file:
        for v, l, d in zip(vysky, data, dlzky):
            file.write(f"{l[0]};{v};{d}\n")


def info(data: list):
    # Pocitanie dlzok, vysok a vytvaranie zoznamu vsetkych vysiek
    vysky = []
    dlzky = []
    total_v = 0
    total_d = 0
    nastupana_vyska = 0
    naklesana_vyska = 0
    for i, l in enumerate(data):
        total_v += l[1]
        total_d += l[2]
        vysky.append(total_v)
        dlzky.append(total_d)
        if i != 0 and l[1] > 0:
            nastupana_vyska += l[1]
        elif i != 0:
            naklesana_vyska -= l[1]
    return vysky, dlzky, nastupana_vyska, naklesana_vyska


def naj(vysky: list, data: list) -> list:
    # Zistovanie najnizsieho a najvyssieho miesta a jeho vysku
    najvyssie_metre = max(vysky)
    najvyssie_meno = data[vysky.index(najvyssie_metre)][0]
    najnizsie_metre = min(vysky)
    najnizsie_meno = data[vysky.index(najnizsie_metre)][0]
    return [[najnizsie_meno, najnizsie_metre], [najvyssie_meno, najvyssie_metre]]


def pisanie_info(najn, najv, dlzky, nast_v, nakl_v):
    # Vytvaranie textov v lavo hore o udajoch trasy
    c.create_text(50, 50, text=f"Dlzka trasy: {dlzky[-1]} km", anchor="w")
    c.create_text(50, 75, text=f"Nastupana vyska: {nast_v} m", anchor="w")
    c.create_text(50, 100, text=f"Naklesana vyska: {nakl_v} m", anchor="w")
    c.create_text(50, 125, text=f"Najvyssie miesto: {najv[0]}, {najv[1]} m", anchor="w")
    c.create_text(50, 150, text=f"Najnizsie miesto: {najn[0]}, {najn[1]} m", anchor="w")


def kresli(data, vysky):
    # Hlavny loop na kreslenie grafickeho profilu trasy
    x, y = 30, 400
    for i, l in enumerate(data):
        vyska = vysky[i]
        if i != 0:
            c.create_line(x, y, x + l[2] * 23, y - l[1])
            x += l[2] * 23
            y -= l[1]
        c.create_oval(x - 4, y - 4, x + 4, y + 4, fill="green")
        c.create_text(x, y + 7, text=f"{l[0]}", font="arial 12", anchor="e", angle=90)



def main():
    global data
    # Ma za ulohu spustat ine funkcie a posielat im udaje, potom handling mouse movementu
    data = read_file()
    vysky, dlzky, nast_v, nakl_v = info(data)
    pisanie_info(*naj(vysky, data), dlzky, nast_v, nakl_v)
    kresli(data, vysky)

x_mouse, y_mouse = 0, 0
def mouse(event):
    global x_mouse, y_mouse
    x_mouse = event.x
    y_mouse = event.y


c.bind("<Motion>", mouse)


main()

while True:
    c.delete('temp')
    if 200 < y_mouse < 600:
        lenght = round((x_mouse - 30) / 23, 2)
        hight = abs(y_mouse - 400 - data[0][1])
        c.create_line(x_mouse, 0, x_mouse, 1000, tag='temp', fill='grey')
        c.create_line(0, y_mouse, 2000, y_mouse, tag='temp', fill='grey')
        c.create_text(x_mouse + 50, y_mouse - 50, text=f"{lenght} km", tag='temp')
        c.create_text(x_mouse + 50, y_mouse - 35, text=f"{+hight} m", tag='temp')

    c.update()
    c.after(10)



c.mainloop()
