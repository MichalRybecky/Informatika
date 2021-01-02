kod = [" ", "ABC", "DEF", "GHI", "JKL",
       "MNO", "PQR", "STU", "VWX", "YZ"]
sifra = "" # vysledna sifra
najcast = [0] * 10 # list pre udaje najcastejsieho policka
message = (input("Zadaj spravu na zasifrovanie: ")).upper()

for char in message:
    # ascii kontrola, ci pismeno je A-Z alebo " "
    if not 64 < ord(char) < 91 and char != " ":
        print(f"Neplatny znak v sprave! Znak: {char}")
    for i, char_group in enumerate(kod):
        if char in char_group:
            najcast[i] += 1 # char_group.index(char) + 1
            # v pripade, ze pri pismene napr. C je zvolenie 1. policka jeden krat, ma tu byt cislo 1
            # ak by C znamenalo zvolenie 1. policka 3x, treba zmazat c. 1 a odkomentovat kod za nim
            sifra += ((char_group.index(char) + 1) * str(kod.index(char_group))) + " "
            break

print(f"Najcastejsie zvolene policko: {najcast.index(max(najcast))}")
print(sifra)
