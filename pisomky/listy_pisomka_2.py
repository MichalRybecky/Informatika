mesta = input("Napis hlavne mesta, ktore si navstivil, oddel ich medzerou: ")
mesta = mesta.split(" ")
mesta.sort()
print(f"Pocet navstivenych hlavnych miest: {len(mesta)}")
print("Abecedne zoradene hlavne mesta: ")
for mesto in mesta:
    print(mesto, end=" ")
