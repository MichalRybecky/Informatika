with open('slovicka.txt', 'r') as file:
    slovicka = [x.strip() for x in file.readlines()]

slovicka = [slovicka[x:x+2] for x in range(0, len(slovicka), 2)]

eng_svk = input('Chces prve Slovenske (S) alebo Anglicke (A) slovicka? ')

i = 0
zle = 0
if eng_svk == 'S':
    control1, control2 = 0, 1
else:
    control1, control2 = 1, 0

while slovicka:
    if i >= len(slovicka):
        i = 0
    odpoved = input(f'{slovicka[i][control1]}, preklad: ')
    if odpoved.lower() == slovicka[i][control2]:
        print('Spravne')
        slovicka.pop(i)
    else:
        print('Nespravne')
        zle += 1
        i += 1

print(f'Pocet nespravnych odpovedi: {zle}')
