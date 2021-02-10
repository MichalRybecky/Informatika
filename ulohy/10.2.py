import random
import tkinter

c = tkinter.Canvas(height=1000, width=1500, bg="white")
c.pack()

switch = True


def hod():
    return [random.randint(1, 6) for _ in range(3)]


def zapis_do_suboru(hody):
    with open("hody_kockou.txt", "w") as file:
        for hod in hody:
            file.write(f"{hod[0]} {hod[1]} {hod[2]}\n")


def kresli(hody):
    global switch
    x, y = 100, 700
    c.delete('all')
    for hodnota, spolu in hody.items():
        vyska = 600 // max(hody.values())
        c.create_text(x, y + 50, text=hodnota)
        c.create_rectangle(x - 10, y, x + 10, y - (spolu * vyska), fill="green")
        percento = (spolu / sum(hody.values()) * 100)
        if switch:
            text = f"{round(percento, 2)}%"
        else:
            text = spolu
        c.create_text(x, y - (spolu * vyska) - 30, text=text, angle=90)
        x += 85


def main():
    hodov = int(entry1.get())
    hody_file = []
    hody = {x: 0 for x in range(3, 19)}
    for i in range(hodov):
        current_hod = hod()
        hody[sum(current_hod)] += 1
        hody_file.append(current_hod)
        kresli(hody)
        c.update()
        c.after(10)
    zapis_do_suboru(hody_file)


def switch():
    global switch
    switch = True if switch == False else False


c.create_text(750, 980, text="Pocet hodov:")
entry1 = tkinter.Entry()
entry1.pack()
button_over = tkinter.Button(text="Start", command=main)
button_over.pack()
button_over = tkinter.Button(text="Switch", command=switch)
button_over.pack()

c.mainloop()
