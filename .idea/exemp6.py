#if
#else
idade = int(input("digite sua idade: "))
if idade >=18:
    print("adulto")
elif idade < 0:
    print("impossivel. não entra")
elif idade >=100:
    print("demasiado velh0")
else:
    print("criança. tens de ser adulto para entrar")

print("---------------------------------")
resposta= input("gostaria de comida? (Y/N)")
if resposta == "Y":
    print("comida")
else:
    print("morre a fome")

print("---------------------------------")
nome = input("digite seu nome: ")
if nome == "":
    print("sem nome")
else:
    print(f"boas, {nome}")

print("---------------------------------")
para_venda = True
if para_venda:
    print("este item é para venda")
else:
    print("este item NÃO é para venda")

print("---------------------------------")
online = True
if online:
    print("o utilizador está ONline")
else:
    print("o utilizador está OFFline")
