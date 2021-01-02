kod, obs, message = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"], [0] * 10, input("Zadaj spravu na zasifrovanie: ")
for char in message:
    for i, char_group in enumerate(kod):
        if char in char_group:
            obs[i] += 1
            print((char_group.index(char) + 1) * str(kod.index(char_group)), end=" ")
print(f"\nNajcastejsie zvolene policko: {obs.index(max(obs))}")
