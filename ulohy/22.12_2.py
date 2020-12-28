import tkinter
from functools import partial

c = tkinter.Canvas(height=500, width=300)
c.pack()

text = '0'
old_op = ''
old_text = ''

def text_add(num):
    global text
    text = '' if text == '0' else text
    text += str(num)


def do(operator):
    global text, old_op, old_text
    if operator == '=':
        if old_op == '+':
            text = int(old_text) + int(text)
        elif old_op == '-':
            text = int(old_text) - int(text)
    elif operator == '+':
        old_op = '+'
        old_text = text
        text = '0'
    elif operator == '-':
        old_op = '-'
        old_text = text
        text = '0'
    elif operator == 'c':
        text = '0'


button0 = tkinter.Button(text=0, command=partial(text_add, 0))
button1 = tkinter.Button(text=1, command=partial(text_add, 1))
button2 = tkinter.Button(text=2, command=partial(text_add, 2))
button3 = tkinter.Button(text=3, command=partial(text_add, 3))
button4 = tkinter.Button(text=4, command=partial(text_add, 4))
button5 = tkinter.Button(text=5, command=partial(text_add, 5))
button6 = tkinter.Button(text=6, command=partial(text_add, 6))
button7 = tkinter.Button(text=7, command=partial(text_add, 7))
button8 = tkinter.Button(text=8, command=partial(text_add, 8))
button9 = tkinter.Button(text=9, command=partial(text_add, 9))
button_plus = tkinter.Button(text='+', command=partial(do, '+'))
button_minus = tkinter.Button(text='-', command=partial(do, '-'))
button_equal = tkinter.Button(text='=', command=partial(do, '='))
button_clear = tkinter.Button(text='C', command=partial(do, 'c'))

button0.pack(side='left')
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
button4.pack(side='left')
button5.pack(side='left')
button6.pack(side='left')
button7.pack(side='left')
button8.pack(side='left')
button9.pack(side='left')
button_plus.pack(side='right')
button_minus.pack(side='right')
button_equal.pack(side='right')
button_clear.pack(side='right')

while True:
    c.delete('all')
    c.create_text(150, 50, text=text)
    c.update()
    c.after(100)

c.mainloop()
