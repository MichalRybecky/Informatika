import tkinter

c = tkinter.Canvas(height=750, width=1000)
c.pack()


def citaj():
    with open("anketa.txt", "r") as file:
        data = [x.strip() for x in file.readlines()]
    data[1] = [int(x) for x in data[1].split()]
    return data


def vykresli():
    c.delete("all")
    data = citaj()
    c.create_text(500, 200, text=data[0], font="arial 30")

    dokopy = sum(data[1])

    x, y = 300, 350
    for hlas in data[1]:
        farba = "grey"
        if hlas == max(data[1]):
            farba = "green"
        c.create_text(x, y, anchor="w", text=hlas, font="arial 30")

        x_2 = x+70 + (int(hlas) * 100 / dokopy * 5)

        c.create_rectangle(x + 70, y - 20, x_2, y + 20, fill=farba)
        y += 100


def key_press(event):
    approved = ["1", "2", "3"]
    if event.char not in approved:
        return
    data = citaj()
    data[1][int(event.char) - 1] += 1

    with open("anketa.txt", "w") as file:
        file.write(f"{data[0]}\n")
        for num in data[1]:
            file.write(f"{num} ")
    vykresli()


vykresli()

c.bind_all("<Key>", key_press)
c.mainloop()
