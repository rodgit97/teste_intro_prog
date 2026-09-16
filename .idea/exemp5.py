amigos = 5
"""
amigos = amigos + 1
amigos += 1
"""
#amigos = amigos -2
"""
amigos -=2
amigos = amigos * 3
amigos *= 3"""
amigos = amigos / 2
amigos /=2
amigos = amigos ** 2
amigos **=2
relembrar = amigos % 2

print(amigos)
print(relembrar)

print("--------------------------")
x= 3.14
y=4
z=5
#resultado=round(x)
#resultado = abs(y)
#resultado= pow(4,3)
#resultado=max(x,y,z)
resultado=min(x,y,z)


print(resultado)
print("--------------------------")
import math
a = 9
print(math.pi)
print(math.e)

resultado = math.sqrt(a)
print(resultado)

resultado = math.ceil(a)
print(resultado)

resultado = math.floor(a)
print(resultado)

print("--------------------------")
import math
radio = float(input("poe o radio de um circulo: "))
circumferencia = 2 * math.pi * radio

print(circumferencia)
print(f" {round(circumferencia, 2)}cm")

print("--------------------------")
import math
radius = float(input("poe o radius dum circulo: "))
area_circulo = math.pi * pow(radius, 2)

print(f"a area de um circulo e: {round(area_circulo,2)} cm ")

print("--------------------------")

a = float(input("da um lado A: "))
b = float(input("da um lado b: "))
c=math.sqrt(pow(a,2) + pow(b,2))
print(f"side c = {c}")

