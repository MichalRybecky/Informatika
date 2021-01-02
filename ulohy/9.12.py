key = list(input("Zadaj sifrovaci kluc: "))
mess = list(input("Zadaj spravu: "))
output = ''
i = 0

for char in mess:
    # reset pohybu cez key zoznam
    if i == len(key):
        i = 0
    # char je male pismeno, prebieha posun
    if 97 <= ord(char) <= 122:
        posun = ord(key[i]) - 97
        char = ord(char) + posun + 1
        if char > 122:
            char -= 25
        output += chr(char)
    # char nie je male pismeno, ide rovno do outputu
    else:
        output += char
    i += 1

print(output)
