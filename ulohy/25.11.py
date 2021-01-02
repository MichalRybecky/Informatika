with open('meteo_stanice.txt', 'r') as file:
    data = [x.strip().split() for x in file.readlines()]

# pocet merani
print(f'Pocet merani: {len(data)}')

# iba namerane teploty
teploty = []
for meranie in data:
    teplota = meranie[3].replace(',', '.')
    if teplota[0] == '+':
        teplota = float(teplota[1:])
    else:
        teplota = -(float(teplota[1:]))
    teploty.append(teplota)
print(f'Namerane teploty: {teploty}')

# max teplota
max_teplota = max(teploty)
if max_teplota < 0:
    max_teplota = str(max_teplota)
    max_teplota = '-' + max_teplota.replace('.', ',')
else:
    max_teplota = str(max_teplota)
    max_teplota = '+' + max_teplota.replace('.', ',')
# max stanica
max_stanica = [meranie[0] for meranie in data if max_teplota == meranie[3]]
print(f'Najvyssie namerana teplota: {max_teplota}, stanica: {max_stanica}')

# priemerna teplota
priemerna_teplota = sum(teploty) / len(teploty)
print(f'Priemerna teplota stanic je {priemerna_teplota:2.2f} stupna.')
