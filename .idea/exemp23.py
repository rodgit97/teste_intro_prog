#quiz
questoes=("quantos elementos estão na tabela periodica? ",
          "qual animal que põe os maiores ovos? ",
          "Qual é o gás mais abundante da atmosfera do pleneta Terra? ",
          "Quantos ossos estão no corpo humano? ",
          "Qual é o planeta mais quente no sistema solar?")

opcoes = (("A. 166","B. 117","C. 118","D. 119"),
("A. baleia","B. Crocodilo","C. Elefante","D. Avestruz"),
("A. Nitrogenio","B. Oxigenio","C. Dioxido-Carbono","D. Hidrogenio"),
("A. 206","B. 207","C. 208","D. 209"),
("A. Mercurio","B. Venus","C. Terra","D. Marte"))

respostas = ("C","D","A","A","B")
palpites=[]
pontuacao=0
numero_questoes=0

for questao in questoes:
    print("-------//--------")
    print(questao)
    for opcao in opcoes[numero_questoes]:
        print(opcao)

    palpite = input("Qual palpite?(A,B,C,D)").upper()
    palpites.append(palpite)
    if palpite == respostas[numero_questoes]:
        pontuacao+=1
        print("CERTO")
    else:
        print("ERRADO")
        print(f"{respostas[numero_questoes]} é a resposta certa.")
    numero_questoes +=1

print("-----------------------------")
print("RESULTADOS")
print("-----------------------------")
print("respostas: ", end="")
for resposta in respostas:
    print(resposta, end="")
print()

print("palpites: ", end="")
for palpite in palpites:
    print(palpite, end="")
print()

pontuacao = int(pontuacao/ len(questoes) * 100)
print(f"tua pontuação: {pontuacao} %")