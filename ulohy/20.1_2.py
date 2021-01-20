import tkinter

c = tkinter.Canvas(height=500, width=1000)
c.pack()

text = input("Zadaj vyraz: ")
prava = len([znak for znak in text if znak == ")"])
lava = len([znak for znak in text if znak == "("])

farby = ("red", "blue", "green", "yellow", "orange", "brown", "purple", "pink")

if prava == lava:
    x = 500 - len(text) * 20 / 2
    y, n = 100, 0
    for znak in text:
        if znak == "(":
            farba = farby[n]
            n += 1
        elif znak == ")":
            n -= 1
            farba = farby[n]
        else:
            farba = "black"
        c.create_text(x, y, text=znak, fill=farba, font="arial 40")
        x += 20
    c.create_text(500, 300, text="Zatvorkovanie je spravne!", font="arial 40")
else:
    c.create_text(500, 250, text="Zatvorkovanie nie je spravne!", font="arial 50")

c.mainloop()
