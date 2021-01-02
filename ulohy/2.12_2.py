with open('text_2.12_2.txt', 'r') as file:
    text = [x for x in file.read()]

print(''.join(text))


def pocet_vyskytov(znak):
    total = 0
    for char in text:
        if char == znak.lower():
            total += 1
    return total


nepouzite = []
for char in range(97, 123):
    pismeno = chr(char)
    total = pocet_vyskytov(pismeno)
    if total != 0:
        print(f'\'{pismeno}\' - {total}')
    else:
        nepouzite.append(pismeno)

nepouzite = ', '.join(nepouzite)
print(f'Nepouzite pismena: {nepouzite}')

