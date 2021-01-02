import tkinter

c = tkinter.Canvas()
c.pack()

trasa = (0, 100, 50, 20, 100, 80, 150, 50, 200, 100, 250, 110, 300, 40)

c.create_line(trasa)

klesanie = 0
stupanie = 0
celkom = 0

for i in range(len(trasa) // 2 - 1):
    bod = 2 * i
    celkom += ((trasa[bod] - trasa[bod + 2]) ** 2 + (trasa[bod + 3]) ** 2) ** 0.50
    d = trasa[bod + 3] - trasa[bod + 1]
    if d < 0:
        stupanie += d
    else:
        klesanie += d

print(-stupanie, klesanie)

c.mainloop()
