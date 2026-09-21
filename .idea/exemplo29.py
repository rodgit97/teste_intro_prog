import random
print("\u25CF ""comunismo é mau")
print("\u25CF ""socialismo é mau")
print("\u25CF ""facismo é mau")
print("\u25CF ""nazismo é mau")
print("\u25CF ""salazarismo é bom")

arte_dado={
    1:("|------------------|",
       "|                  |",
       "|         ●        |",
       "|                  |",
       "|__________________|"),
    2:("|------------------|",
       "|   ●              |",
       "|                  |",
       "|             ●    |",
       "|__________________|"),
    3:("|------------------|",
       "|   ●              |",
       "|         ●        |",
       "|              ●   |",
       "|__________________|"),
    4:("|------------------|",
       "|   ●         ●    |",
       "|                  |",
       "|   ●         ●    |",
       "|__________________|"),
    5: ("|------------------|",
        "|   ●         ●    |",
        "|        ●         |",
        "|   ●         ●    |",
        "|__________________|"),
    6:("|------------------|",
       "|   ●          ●   |",
       "|   ●          ●   |",
       "|   ●          ●   |",
       "|__________________|"),
}
dado=[]
total=0
numero_do_dado= int(input("quantos dados? "))

for die in range(numero_do_dado):
    dado.append(random.randint(1,6))

for die in range(numero_do_dado):
    for line in arte_dado.get(dado[die]):
        print(line)

for line in range(5):
    for die in dado:
        print(arte_dado.get(die)[line], end='')

for die in dado:
    total += die

print(f"o total :{total}")

