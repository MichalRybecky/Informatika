import random

stud = int(input("Zadaj pocet studentov: "))
ot = int(input("Zadaj pocet otazok: "))

studenti = [(student + 1) for student in range(stud)]
otazky = [(otazka + 1) for otazka in range(ot)]

if ot < stud:
    print("Error: Pocet otazok mensi ako pocet studentov.")
for i in range(stud):
    student = studenti[random.randrange(len(studenti))]
    otazka = otazky[random.randrange(len(otazky))]
    studenti.remove(student)
    otazky.remove(otazka)
    print(f"1. odpoved: student {student} otazka c. {otazka}")

