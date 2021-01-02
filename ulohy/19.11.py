# Otvaranie suboru s udajmi
with open('prihlaseni.txt', 'r') as file:
    udaje = [udaj.strip('\n') for udaj in file.readlines()]
print(f'Pocet prihlasenych osob: {int(len(udaje) / 2)}')

menej_ako_15 = 0
priemerny_vek = 0
for i in range(len(udaje) // 2):
    vek = int(udaje[i * 2 + 1])
    priemerny_vek += vek
    if vek < 15:
        menej_ako_15 += 1
print(f'Pocet osob do 15 rokov: {menej_ako_15}')

listok = float(input('Zadaj cenu listka pre jednu osobu: '))
cena = int(((len(udaje) // 2) - menej_ako_15) * listok + menej_ako_15 * (listok * 0.5))
print(f'Cestovne: {cena}€.')

priemerny_vek /= (len(udaje) // 2)
print(f'Priemerny vek osob: {priemerny_vek} rokov.')
