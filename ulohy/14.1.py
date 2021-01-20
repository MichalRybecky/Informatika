import tkinter
import random

c = tkinter.Canvas(height=300, width=600)
c.pack()


def over():
    zadane = int(entry1.get()) if entry1.get() != '' else 0
    if zadane == delenec // delitel:
        c.create_text(50, 125, anchor='w', font='arial 30', text='Spravne')
    else:
        c.create_text(50, 125, anchor='w', font='arial 30', text='Nespravne')

    farby = ('green', 'blue', 'red')
    zvysok = 'yellow'
    x = 50
    farba_control = 0
    for i in range(delenec):
        if i % delitel == 0:
            farba_control += 1
        if farba_control == 3:
            farba_control = 0
        farba = farby[farba_control]
        if (delenec // delitel) * delitel <= i:
            farba = zvysok
        c.create_oval(x-5, 150, x+5, 160, fill=farba)
        x += 15


def novy_priklad():
    global delenec, delitel
    c.delete('all')
    delenec = random.randint(11, 30)
    delitel = random.randint(2, 9)
    c.create_text(50, 50, anchor='w', font='arial 40', text=f'{delenec} : {delitel} =')


entry1 = tkinter.Entry()
entry1.pack()
button_over = tkinter.Button(text="Over", command=over)
button_over.pack()
button_over = tkinter.Button(text="Novy priklad", command=novy_priklad)
button_over.pack()
novy_priklad()

c.mainloop()
