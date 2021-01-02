import random
import tkinter

c = tkinter.Canvas(width=750, height=750)
c.pack()


def main():
    x = random.randint(50, 700)
    secret_key = chr(random.randint(97, 122))
    y = -100
    while True:
        if key == secret_key:
            main()
        if y == 695:
            break
        game_loop(x, y, secret_key)
        y += 5


def key(event):
    global key
    key = event.char


def game_loop(x, y, secret_key):
        c.create_rectangle(0, 0, 750, 750, fill='white')
        c.create_oval(x-50, y-60, x+50, y+60, width=2, outline='black', fill='#fffccc')
        if y > 500:
            c.create_text(x, y, text=secret_key, font='arial 30 bold')
        c.update()
        c.after(15)


c.bind_all('<Key>', key)
main()
c.mainloop()
