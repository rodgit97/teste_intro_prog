import random
#print(help(random))

number = random.randint(1,6)
print(number)

print("---------------")
baixa = 1
alta=100
number = random.randint(baixa,alta)
print(number)

print("---------------")
baixa = 1
alta=100
number = random.random()
print(number)
print("---------------")
baixa = 1
alta=100
opcoes =("pedra", "papel", "tesoura")
opcao = random.choice(opcoes)
print(opcao)

print("---------------")
baixa = 1
alta=100
opcoes =("pedra", "papel", "tesoura")
cartas= ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
carta = random.shuffle(cartas)
print(carta)