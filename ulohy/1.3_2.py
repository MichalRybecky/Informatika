with open('skok_do_dialky.txt', 'r') as file:
    data = [x.strip().split() for x in file.readlines()]

krajiny = [x[1] for x in data]
print(f"Krajiny zucastnenych sportovcov: {', '.join(krajiny)}.")

krajiny_pocty = {}
for i in krajiny:
    if i not in krajiny_pocty:
        krajiny_pocty[i] = 1
        continue
    krajiny_pocty[i] += 1

for i in krajiny_pocty:
    print(f"Krajina: {i}, pocet: {krajiny_pocty[i]}.")

max_c = 0
for i in data:
    max_skok = int(max(i[2:]))
    if max_skok > max_c:
        max_m = i[0]
        max_c = int(max(skoky))
    elif max_skok == max_c:
        max_m += ", " + i[0]

print(f"Najdalej skocil(i) {max_m}, so vzdialenostou {max_c}m.")

