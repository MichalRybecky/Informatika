with open('hada.txt', 'r') as file:
    hry = [x.strip() for x in file.readlines()]

print(f'Pocet zapisanych hier v subore: {len(hry)}')
print(f'Najdlhsia hra mala {len(max(hry, key=len))} krokov.')


def skratit(hra):
    predosle = hra[0]
    skratene = ''
    count = 0
    for krok in hra:
        if predosle != krok:
            skratene += f'{predosle} {count} '
            count = 0
            predosle = krok
        count += 1
    skratene += f'{predosle} {count}\n'
    return skratene


with open('hada_copy.txt', 'w') as file:
    for hra in hry:
        file.write(skratit(hra))
