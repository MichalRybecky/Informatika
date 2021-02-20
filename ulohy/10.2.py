import random
import tkinter

c = tkinter.Canvas(height=1000, width=1500, bg="white")
c.pack()

switch = True


def hod(kociek):
    return [random.randint(1, 6) for _ in range(kociek)]


def zapis_do_suboru(hody):
    with open("hody_kockou.txt", "w") as file:
        for hod in hody:
            for h in hod:
                file.write(f"{h} ")
            file.write("\n")


def kresli(hody):
    global switch
    y = 700
    space = 1400 / len(hody)
    x = space
    c.delete("all")
    for hodnota, spolu in hody.items():
        vyska = 600 // max(hody.values())
        c.create_text(x, y + 50, text=hodnota)
        c.create_rectangle(x - 10, y, x + 10, y - (spolu * vyska), fill="green")
        percento = spolu / sum(hody.values()) * 100
        if switch:
            text = f"{round(percento, 2)}%"
        else:
            text = spolu
        c.create_text(x, y - (spolu * vyska) - 30, text=text, angle=90)
        x += space


def main():
    hodov = int(entry1.get())
    kociek = int(entry2.get())
    hody_file = []
    hody = {x: 0 for x in range(kociek, (kociek * 6) + 1)}
    for i in range(hodov):
        current_hod = hod(kociek)
        hody[sum(current_hod)] += 1
        hody_file.append(current_hod)
        kresli(hody)
        c.update()
        c.after(10)
    zapis_do_suboru(hody_file)


def switch():
    global switch
    switch = True if switch == False else False


entry1 = tkinter.Entry()
entry1.pack()
entry2 = tkinter.Entry()
entry2.pack()
button_over = tkinter.Button(text="Start", command=main)
button_over.pack()
button_over = tkinter.Button(text="Switch", command=switch)
button_over.pack()

c.mainloop()
