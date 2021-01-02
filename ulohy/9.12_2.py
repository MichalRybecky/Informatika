with open('hlasovanie.txt', 'r') as file:
    hlasovanie_vstup = [x.strip() for x in file.readlines()]

with open('zrusene.txt', 'r') as file:
    zrusene_vstup = [x.strip() for x in file.readlines()]

# celkovy pocet hlasov
print(f'Celkovy pocet hlasovani: {len(hlasovanie_vstup)}')

# kolko hlasov dostal kazdy zo zajazdov
hlasy = []
[hlasy.append(x) for x in hlasovanie_vstup if x not in hlasy]
hlasy_final = [[x, 0] for x in hlasy]
for hlas in hlasy_final:
    for hlas2 in hlasovanie_vstup:
        if hlas[0] == hlas2:
            hlas[1] += 1
[print(f'Zajazd: {x[0]}, hlasov: {x[1]}') for x in hlasy_final]

# ktory zajazd dostal najmenej hlasov
najmenej_c = min(x[1] for x in hlasy_final)
najmenej = ', '.join([x[0] for x in hlasy_final if x[1] == najmenej_c])
print(f'Zajazd s najmenej hlasmi: {najmenej}: {najmenej_c}')

# ktory zajazd dostal najviac hlasov
najviac_c = max(x[1] for x in hlasy_final)
najviac = ', '.join([x[0] for x in hlasy_final if x[1] == najviac_c])
print(f'Zajazd s najmenej hlasmi: {najviac}: {najviac_c}')

# kolko hlasov dostali zrusene zajazdy spolu
zrusene_spolu = 0
for hlas in hlasy_final:
    if hlas[0] in zrusene_vstup:
        zrusene_spolu += hlas[1]
print(f'Zrusene zajazdy spolu dostali {zrusene_spolu} hlasov.')
