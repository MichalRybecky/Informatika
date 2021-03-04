with open("objednane_jedla.txt", "r") as file:
    data = [x.strip().split() for x in file.readlines() if x != "\n"]

print(f"Celkovy pocet objednanych jedal: {len(data)}.")

farby = {"z": 0, "c": 0, "m": 0, "o": 0}
for i in data:
    farby[i[1]] += 1

nedostatok = []
for farba in farby:
    print(f"Farba \"{farba}\": pocet jedal: {farby[farba]}.")
    if int(farby[farba]) < 20:
        nedostatok.append(farba)

print(f"Farby s nedostatocnym poctom objednani: {', '.join(nedostatok)}.")
if nedostatok == []:
    print("Vsetky jedla maju dostatocne vela objednavok.")
