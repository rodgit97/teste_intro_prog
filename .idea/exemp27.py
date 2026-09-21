#numeros aleatorios
import random

numero_mais_baixo = 1
numero_mais_alto = 100
resposta = random.randint(numero_mais_baixo, numero_mais_alto)
palpites =0
a_carregar = True

print(resposta)
print("python palpite do numero do jogo")
print(f"selecionar um numero entre {numero_mais_baixo} e {numero_mais_alto}")

while a_carregar:
    palpite = input("Digite o seu palpite: ")
    if palpite.isdigit():
        palpite = int(palpite)
        palpites += 1

        if palpite <  numero_mais_baixo or palpite > numero_mais_alto:
            print(f"porfavor seleciona um numero entre {numero_mais_baixo} e {numero_mais_alto}")
        elif palpite < resposta:
            print("demasiado baixo, de NOVO")
        elif palpite > resposta:
            print("demasiado alto, de NOVO")
        else:
            print(F"CERTO A RESPOSTA ERA {resposta}")
            print(F"numero de palpites {palpites}")
            a_carregar = False
    else:
        print("palpite invalido")
        print(f"por-favor seleciona um numero entre  {numero_mais_baixo} e {numero_mais_alto}")


