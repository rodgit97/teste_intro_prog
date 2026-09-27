# hangman game
from exemp44lista import palavras
import random

#palavras = ("maça" , "laranja", "banana", "coco", "ananas")

#dicionario da chave :()
arte_enforcamento={0: ("   ",
                       "   ",
                       "   "),
                   1: (" o ",
                       "   ",
                       "   "),
                   2: (" o ",
                       " | ",
                       "   "),
                   3: (" o ",
                       "/| ",
                       "   "),
                   4: (" o ",
                       "/|\\",
                       "   "),
                   5: (" o ",
                       "/|\\",
                       "/  "),
                   6: (" o ",
                       "/|\\",
                       "/ \\ ")}
"""
for linha in arte_enforcamento[6]:
    print(linha)
    """
#print(arte_enforcamento[0])

def homem_exibicao(palpites_errados):
    print("************")
    for linha in arte_enforcamento[palpites_errados]:
        print(linha)
    print("************")

    #pass

def exibir_dica(sugestao):
    print(" ".join(sugestao))
    #pass
def exibir_resposta(resposta):
    print(" ".join(resposta))

    #pass

def main():
    resposta = random.choice(palavras)
    print(resposta)#da uma palavra aleatoriamente
    sugestao =['_'] * len(resposta)
    print(sugestao)# da espaços para palavra
    palpites_errados = 0
    letras_adivinhadas = set()
    em_execucao = True

    #while em_execucao == True:
    while em_execucao:
        homem_exibicao(palpites_errados)
        exibir_dica(sugestao)
       # exibir_resposta(resposta)
        palpite = input("digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("entrada invalida")
            continue

        if palpite in letras_adivinhadas:
            print(f"{palpite} já foi adivinhada")
            continue

        letras_adivinhadas.add(palpite)


        if palpite in resposta:
            for i in range(len(resposta)):
                if resposta[i]== palpite:
                    sugestao[i] = palpite
        else:
            palpites_errados += 1

        if "_" not in sugestao:
            homem_exibicao(palpites_errados)
            exibir_resposta(resposta)
            print("GANHOU")
            em_execucao = False
        #elif palpites_errados >= len(homem_exibicao) - 1:
         #   homem_exibicao(palpites_errados)
          #  exibir_resposta(resposta)
           # print("PERDEU")
            #em_execucao = False


    #pass

if __name__ == "__main__":
    main()