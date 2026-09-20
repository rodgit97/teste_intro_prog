##20 (02:17:28) nested loops ➿
for x in range(1,10):
    print(x)

print("---------------------")
for x in range(1, 10):
    print(x, end=" ")

print("---------------------")
for x in range(1, 10):
    print(x, end=" \n")

print("---------------------")
for x in range(3): #repete os elementos 3 vezes
    for y in range(1, 10):
        print(y, end="")

print("---------------------")

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")

print("---------------------")
for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()# repete mas com paragrafos

print("---------------------")
linha_row = int(input("insira o numero das linhas: "))
coluna_column = int(input("insira o numero das colunas: "))
simbolo = input("insira o simbolo para usar: ")

for x in range(linha_row):
    for y in range(coluna_column):
        print(simbolo, end="")
    print()

print("---------------------")