import tkinter
c = tkinter.Canvas(height=250, width=500)
c.pack()

with open('zastavba_na_ulici.txt', 'r') as file:
    data = [x.strip().split() for x in file.readlines()]


def kresli_ciaru(x, y, x1, y1):
    c.create_line(x, y, x1, y1, fill='red')


def nakresli():
    c.create_rectangle(0, 0, 500, 250, fill='white')
    x = 2
    y = 200
    max_vyska = int(entry1.get())

    for i, sur in enumerate(data):
        sirka = int(sur[0])
        vyska = int(sur[1])
        farba = 'grey'
        outline = 'black'
        if vyska == 0:
            farba = 'green'
            outline = 'green'
        if abs(int(data[i-1][1]) - vyska) > max_vyska:
            kresli_ciaru(x, y - vyska, x, y - int(data[i-1][1]))
        c.create_rectangle(x, y, x + sirka, y - vyska, fill=farba, outline=outline)
        x += sirka


entry1 = tkinter.Entry()
button1 = tkinter.Button(text='Sup',command=nakresli)
entry1.pack()
button1.pack()
c.mainloop()
