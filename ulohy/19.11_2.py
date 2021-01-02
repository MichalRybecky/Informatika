with open('sutaz_v_behu.txt', 'r') as file:
    data = [x.strip('').split() for x in file.readlines()]

print(f'Pocet zucastnenych sportovcov: {len(data)}')

cas = int(min(data[1]))
for i in data:
    print(f'Sutaziaci {i[0]} dobehol do ciela za {int(i[1])} sekund.')
    if int(i[1]) == cas:
        meno = i[0]

minuty = cas // 60
sekundy = cas - minuty * 60
print(f'Najlepsi sutaziaci je {meno} s casom {minuty} min. {sekundy} sek.')
