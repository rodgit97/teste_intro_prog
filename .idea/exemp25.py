#concession stand program
menu={"pizza": 3.00,
      "pipocas":4.50,
      "sumo-natural":2.00,
      "chocolate":1.90,
      "batatas_fritas":0.90,
      "amendoins": 1.10,
      "petiscos":2.20
      }

carrinho= []
total=0
print("---MENU---")
for chave, valor in menu.items():
      print(f"{chave}: {valor}")
      print(f"{chave}: {valor:.2f}")
      print(f"{chave:10}: {valor:.2f}")
print("---------------//-------------")

while True:
      comida = input("seleciona um item(q para sair do menu): ")
      if comida == "q":
            break
      elif menu.get(comida) is not None:
            carrinho.append(comida)

print("-------------SEU PEDIDO-----------------")
for comida in carrinho:
      #total = total + menu.get(comida)
      total += menu.get(comida)
      print(comida, end=" ")

print()
print(f"total: {total} €")

