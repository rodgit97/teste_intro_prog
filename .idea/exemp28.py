#rock, paper, scissors game
import random

opcoes = ("pedra", "papel", "tesoura")
jogador= None
computador = random.choice(opcoes)
carregar = True
while carregar:
#while True:

    jogador = None
    computador = random.choice(opcoes)

    while jogador not in opcoes:
        jogador = input("escolhe(pedra, papel, tesoura): ")

    print(f"jogador: {jogador}")
    print(f"computador: {computador}")

    if jogador == computador:
        print("é um empate")
    elif jogador == "pedra" and computador == "tesoura":
        print("ganhou")
    elif jogador == "papel" and computador == "pedra":
        print("ganhou")
    elif jogador == "tesoura" and computador == "papel":
        print("ganhou")
    else:
        print("PERDEU")

    #jogar_de_novo = input("jogar de novo? (s/n): ").lower()=="y":
    if not input("jogar de novo? (s/n): ").lower()=="y":
#if not jogar_de_novo == "s":
    carregar = False

print("obrigado por jodar")

    """if not input("jogar outra vez? (y/n): ").lower() == "y":
        break
"""

    #está tudo errado