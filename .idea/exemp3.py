#input()
nome = input("qual é o seu nome? ")
idade = input("quantos anos tem sua idade? ")

#primeiro faz isto
idade = int(idade)
#apos isto
idade = idade +1

print(f' ola {nome}')
print(f' parabens')
print(f' a sua idade é {idade}')

print("-------------//-----------------")
idade = int(input("quantos anos tens? "))

idade = idade +1

print(f' ola {nome}')
print(f' parabens')
print(f' a sua idade é {idade}')

print("-------------//-----------------")
lenght = float(input("enter the lenght: "))
width = float(input("enter the width: "))
area = lenght * width

print(area)
print(f"the area is: {area} cm")

print("-------------//-----------------")
item = input("what item would you like to buy? ")
price = float(input("what is the price? "))
quantity = int(input("how much do you want to buy? "))
total_price = price * quantity

print(total_price)
print(f"voce comprou {quantity} x {item}/s")
print(f"o total é: ${total_price}")