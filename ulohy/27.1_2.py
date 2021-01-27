veta = "Cez vikend je planovana odstavka tunela pod hradom".split()
print(f'Veta pozostava z {len(veta)} slov.')

nova_veta = ""
for slovo in veta:
    nova_veta += slovo[0].upper() + slovo[1:]

print(nova_veta)

uplne_nova_veta = ""
for pismeno in nova_veta:
    if pismeno.isupper():
        uplne_nova_veta += ' '
    uplne_nova_veta += pismeno.upper()
print(uplne_nova_veta[1:])
