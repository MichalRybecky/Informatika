import tkinter

c = tkinter.Canvas(height=500, width=1000, bg="white")
c.pack()

with open("metro.txt", "r") as file:
    data = [x.strip() for x in file.readlines()]
farba = data[0]
data.pop(0)

x, y = 50, 250
pr_x, pr_y = x, y
for i, stanica in enumerate(data):
    c.create_oval(x - 7, y + 7, x + 7, y + 21, fill=farba, outline="")
    c.create_line(pr_x, pr_y + 15, x, y + 15, width=3, fill=farba)
    if stanica[0] == "*":
        stanica = stanica[1:]
        c.create_oval(x - 5, y + 9, x + 5, y + 19, fill="white", outline="")
    if i == 0 or i == len(data) - 1:
        c.create_rectangle(x - 10, y + 5, x + 10, y + 25, fill=farba, outline="")
    c.create_text(x, y, text=stanica, angle=45, anchor="w", font="arial 13")
    pr_x, pr_y = x + 5, y
    x += 50

c.mainloop()
