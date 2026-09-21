#⭐ shopping cart program 🛒
comidas= []
precos=[]
total=0

while True:
    comida = input("insira a comida para comprar(s para sair): ")
    if comida.lower() == "s":
        break
    else:
        preco = float(input(f"insira o preço do produto {comida}: "))
        comidas.append(comida)
        precos.append(preco)

print("-----------SEU CARRINHO------------------")
for comida in comidas:
    print(comida)

for preco in precos:
    total += preco

print()
print(f"TOTAL DAS COMPRAS: {total} €")