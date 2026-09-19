#while loops

nome = input("Qual o seu nome?")
#repete quando esta vazio
while nome == "":
    print("nao nos deste um nome")
    nome = input("Qual é o seu nome? ")
print(f"boas {nome}")

print("-------------------------")
nome = input("de nos o seu nome? ")
#repete quando esta vazio
while nome == "":
    print("ainda não nos deu um nome")
    nome = input("nos de um nome ou te matamos: ")

print(f"boas {nome}")

print("-------------------------")
idade = int(input("Qual é a sua idade? "))

while idade <0:
    print("és um feto")
    idade = int(input("Qual é a sua idade? "))
print(f"a sua idade é {idade} ano/s")

print("-------------------------")
comida = input("entra comcomida que gosta (q para sair)")

while not comida == "q":
    print(f"gostas de {comida}")
    comida = input("entra comcomida que gosta (q para sair)")
print("adeus")

print("-------------------------")
numero = int(input("entra com um numero # de 1- 10: "))

while  numero < 1 or numero > 10:
    print(f"{numero} não é válido")
    numero = int(input("entra com um numero # de 1- 10: "))

print(f"seu numero é {numero}")

