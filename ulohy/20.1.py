import tkinter

c = tkinter.Canvas(height=200, width=1000, bg='black')
c.pack()

with open('stanice.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]

def main():
    global current, stanice
    c.delete('all')
    for stanica in stanice:
        c.create_text(stanica[1], 100, anchor='w', text=stanica[0], fill='red', font='arial 100 bold')
        stanica[1] -= 5
        if stanica[1] == -len(stanica[0]) * 50:
            stanice.append([data[current], 1000])
        if stanica[1] >= -len(stanica[0]) * 50:
            break
        elif stanica[1] == -2000:
            stanice.remove(stanica)
    if len(stanice) >= 3:
        stanice = [stanice[0], stanice[1]]
    c.update()
    c.after(10, main)


def hore(event):
    global current
    current += 1
    if current == len(data) + 1:
        current = 0
    stanice.append([data[current], 1000])


current = 0
stanice = [[data[current], 1000]]

main()

c.bind('<1>', hore)
c.mainloop()
