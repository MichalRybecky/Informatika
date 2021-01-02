with open('ziaci.txt', 'r') as file:
    mena = [x.strip() for x in file.readlines()]

slicer = int(len(mena) / 2)
mena_1 = mena[:slicer]
mena_2 = mena[slicer:]

print(f'Pocet mien v subore: {slicer}')
print(f'Najdlhsie krstne meno: {max(mena_1, key=len)}')
print(f'Najdlhsie priezvisko: {max(mena_2, key=len)}')

with open('vystup.txt', 'w') as file:
    for krstne, priezvisko in zip(mena_1, mena_2):
        medzery = (20 - len(krstne))
        file.write(str(krstne) + medzery * ' ' + str(priezvisko) + '\n')
