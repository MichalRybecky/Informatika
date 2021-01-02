import random

priklady = []
preskusat = []
body = 0

for _ in range(10):
    num_1 = random.randrange(1, 11)
    num_2 = random.randrange(1, 11)
    priklady.append([num_1, num_2, num_1 * num_2])

for priklad in priklady:
    odpoved = int(input(f'{priklad[0]} * {priklad[1]} = '))
    if odpoved == priklad[2]:
        body += 1
    else:
        preskusat.append(priklad)

for priklad in preskusat:
    int(input(f'{priklad[0]} * {priklad[1]} = '))

print(f'Pocet ziskanych bodov: {body}')

with open('nasobilka_vystup.txt', 'w') as file:
    for priklad in priklady:
        file.write(f'{priklad[0]} * {priklad[1]} = {priklad[2]}\n')
