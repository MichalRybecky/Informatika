import tkinter

c = tkinter.Canvas(height=1000, width=1000)
c.pack()


class Robot:
    """
    hore = 0
    vlavo = 1
    vpravo = 2
    dole = 3
    """
    def __init__(self):
        self.x = 500
        self.y = 500
        self.smer = 0


def vykonaj():
    prikaz = entry1.get().strip().split()
    smery = {
        'vlavo': {0: 1, 1: 3, 3: 2, 2: 0},
        'vpravo': {0: 2, 1: 0, 3: 1, 2: 3}
    }

    if prikaz == []:
        pass
    if prikaz[0] == "chod" or prikaz[0] == "ciara":
        stare_x, stare_y = robot.x, robot.y
        if robot.smer == 0:
            robot.y -= int(prikaz[1])
        elif robot.smer == 3:
            robot.y += int(prikaz[1])
        elif robot.smer == 1:
            robot.x -= int(prikaz[1])
        elif robot.smer == 2:
            robot.x += int(prikaz[1])
        c.create_line(stare_x, stare_y, robot.x, robot.y, width=2)
    else:
        robot.smer = smery[prikaz[0]][robot.smer]


robot = Robot()
entry1 = tkinter.Entry().pack()
button1 = tkinter.Button(text="Vykonaj", command=vykonaj).pack()

c.mainloop()
