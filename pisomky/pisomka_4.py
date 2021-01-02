import tkinter
c = tkinter.Canvas()
c.pack()

with open('postava_pisomka_4.txt', 'r') as file:
    sur = [x.strip('\n') for x in file.readlines()]
sur = tuple(sur)

x = 0
panak = []
for _ in range(len(sur) // 4):
    panak.append((sur[x], sur[x+1], sur[x+2], sur[x+3]))
    x += 4

c.create_oval(panak[0])
panak.remove(panak[0])

for sur in panak:
    c.create_line(sur)

c.mainloop()
