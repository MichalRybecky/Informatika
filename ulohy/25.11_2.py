with open('bus_vytazenost.txt', 'r') as file:
    data = [x.strip().split() for x in file.readlines()]

kapacita = data[0]
data.remove(kapacita)
kapacita = int(kapacita[0])

#Pocet zastavok
print(f'Pocet zastavok: {len(data)}')

# Vsetky zastavky
print(f'Zastavky: ', end = '')
for i in data:
    print(*i[2:], end = ', ')
print()

# Preplnenost
cestujuci = 0
prekrocene = []
print('Preplnene zastavky: ', end = '')
for j in data:
    cestujuci += int(j[0])
    cestujuci -= int(j[1])
    if cestujuci > kapacita:
        print(*j[2:], end = ', ')
        prekrocene.append(cestujuci - kapacita)
print()
print(f'Najvyssia prekrocena kapacita bola o {max(prekrocene)} ludi.')
