import time

time.sleep(3)#segundos

print("começa o tempo")

print("--------------------")

import time
meu_tempo=int(input("insira o tempo em segundos: "))
for x in range (0,meu_tempo):
    print(x)
    time.sleep(3)#segundos

print("CJHEGOU")

print("--------------------")

import time
meu_tempo=int(input("insira o tempo em segundos: "))
for x in range (meu_tempo,0,-1 ):
    print(x)
    time.sleep(1)#segundos

print("CHEGOU")

print("--------------------")

import time
meu_tempo=int(input("insira o tempo em segundos: "))
for x in range (meu_tempo,0,-1 ):
    segundos = x % 60
    print(f"00:00:{segundos} ")
    time.sleep(1)#segundos

print("CHEGOU")

print("--------------------")

import time
meu_tempo=int(input("insira o tempo em segundos: "))
for x in range (meu_tempo,0,-1 ):
    segundos = x % 60
    print(f"00:00:{segundos:02} ")
    time.sleep(1)#segundos

print("CHEGOU")


print("--------------------")

import time
meu_tempo=int(input("insira o tempo em segundos/4: "))
for x in range (meu_tempo,0,-1 ):
    segundos = x % 60
    minutos = int(x / 60)%60
    print(f"00:{minutos:02}:{segundos:02} ")
    time.sleep(1)#segundos

print("CHEGOU")

print("--------------------")

import time
meu_tempo=int(input("insira o tempo em segundos/5: "))
for x in range (meu_tempo,0,-1 ):
    segundos = x % 60
    minutos = int(x / 60)%60
    horas =int(x / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02} ")
    time.sleep(1)#segundos

print("CHEGOU")