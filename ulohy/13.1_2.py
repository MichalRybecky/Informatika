import random

with open('virus1.txt', 'r') as file:
    data = [x.strip().split() for x in file.readlines()]

if random.randrange(2) == 1:
    random.shuffle(data)

for riadok in data:
    if random.choice((True, False)):
        random.shuffle(riadok)
        for i, slovo in enumerate(riadok):
            if random.choice((True, False)):
                riadok[i] = slovo[::-1]

with open('virus2.txt', 'w') as file:
    for riadok in data:
        file.write(f'{" ".join(riadok)}\n')
