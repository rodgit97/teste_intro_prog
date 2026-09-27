#slot machine
import random

def linha_rodativa():
    simbolos= ["o^o", "C|", "()", "n" ,"*"]
    """
    resultados = []
    for simbolo in range(3):
        resultados.append(random.choice(simbolos))
    return resultados
    """
    return[random.choice(simbolos)for _ in range(3)]
    #pass

def imprimir_linha(linha):
    print(" ------------------ ")
    print(" | ".join(linha))
    print(" ------------------ ")

    #pass

def receber_pagamento(linha, aposta):
    if linha[0]== linha[1] == linha[2]:
        if linha[0] == 'o^o':
            return  aposta * 3
        elif linha[0] == 'C|':
            return aposta * 4
        elif linha[0] == '()':
            return aposta * 5
        elif linha[0] == 'n':
            return aposta * 10
        elif linha[0] == '*':
            return aposta * 20
    return 0


    #pass

def main():
    balanco =100
    print("---------------------")
    print("bemvindo ao caca niqueis")
    print("simbolos: o^o  C| () n *")
    print("-----------------------")
    #pass
    while balanco > 0:
        print(f"balanço corrente: {balanco} €")

        aposta = input("Faça a sua aposta: ")

        if not aposta.isdigit():
            print("faz favor de entrar um numero valido")
            continue

        aposta = int(aposta)

        if aposta > balanco:
            print("fundos insuficientes")
            continue

        if aposta <=0:
            print("as apostas devem ser maior que 0")
            continue


        balanco -= aposta

        linha = linha_rodativa()
        #print(linha)
        print("fiacao...\n")

        imprimir_linha(linha)

        pagamento = receber_pagamento(linha,aposta)

        if pagamento >0:
            print(f" GANHOU {pagamento}€")
        else:
            print("PERDEU ESTA RONDA")

        balanco += pagamento

        #jogar_outra_vez = input("quer rodar de novo? (S/N)").upper()
        jogar_outra_vez = input("quer rodar de novo? (S/N)")
        if jogar_outra_vez != 's':
            break

    print(f"----------------------------------------------")
    print(f"Fim do Jogo! O seu balanço final é {balanco} €")
    print(f"----------------------------------------------")

if __name__ == "__main__":
    main()

