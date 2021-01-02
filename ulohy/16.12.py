from random import randint

tipy = list(input("Zadaj svoje tipy (5 cisel oddelenych medzerami): ").split())

if len(tipy) != 5:
    print("Nespravny pocet tipov!")
    exit()

cisla = []
while len(cisla) != 5:
    cislo = randint(1, 35)
    if cislo in cisla:
        continue
    cisla.append(cislo)

print('Vyzrebovane cisla: ' + str(cisla))
uhadol = [int(x) for x in tipy if int(x) in cisla]
print(f'Uhadol si {len(uhadol)} cisla, ktore boli: {uhadol}')

with open('loteria.txt', 'r') as file:
    ucastnici = [x.strip().split() for x in file.readlines()]

uhadli = [0, 0, 0, 0, 0]
for ucastnik in ucastnici:
    u = [x for x in ucastnik if int(x) in cisla]
    if len(u) == 0:
        continue
    uhadli[len(u) - 1] += 1

print(f'Pocet uhadnutych: {uhadli}')
