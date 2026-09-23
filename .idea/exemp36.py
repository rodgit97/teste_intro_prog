#list comprehensions 📃
#doubles
dobros = []
for x in range(1, 11):
    dobros.append(x*2)

print(dobros)
print("-------------------")
doubles = [x*3 for x in range(1, 11)]
print(doubles)
print("-------------------")
doubles = [x*2 for x in range(1, 11)]
triplos = [y *3 for y in range(1, 11)]
quadrados = [z * z  for z in range(1, 11)]
print(doubles)
print(triplos)
print(quadrados)
print("-------------------")
frutas =["maca", "laranja", "banana","morango"]
frutas =[fruta.upper() for fruta in frutas]
print(frutas)

frutas =[fruta[0] for fruta in frutas]
print(frutas)

print("-------------------")
numeros = [1, -2, 3, -4, -5, 6]
numeros_positivos=[numero for numero in numeros if numero >= 0]
numeros_negativos=[numero for numero in numeros if numero < 0]

print(numeros_positivos)
print(numeros_negativos)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)

numeros_impares = [numero for numero in numeros if numero % 2 == 1]
print(numeros_impares)

print("-------------------")

notas = [
    85, 42, 79, 90, 56, 61, 30
]
notas_concluidas = [nota for nota in notas if nota >= 60]
print(notas_concluidas)
