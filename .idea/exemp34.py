#iterables
numeros = [1,2,3,4,5]

for numero in numeros:
 print(numero)

print("---------------")
for numero in reversed(numeros):
  print(numero)

print("---------------")
for numero in reversed(numeros):
   print(numero, end= " ")

print("---------------")
for numero in reversed(numeros):
 print(numero, end=" - ")

print("---------------")
"""
frutos = {"maca", "laranja", "banana","coco"}
for fruto in reversed(frutos):
 print(fruto)
"""
print("---------------")
nome = "codigo morse"
for carater in nome:
 print(carater, end=" - ")
print("---------------")

nome = "codigo morse"
for carater in nome:
 print(carater, end=" ")
print("---------------")

meu_dicionario = {"A":1, "B":2, "C":3, "D":4}
for chave in meu_dicionario:
    print(chave)
print()
for valor in meu_dicionario.values():
    print(valor)
print()
for chave, valor in meu_dicionario.items():
    print(chave, valor)

for chave, valor in meu_dicionario.items():
    print(f"{chave} = {valor}")