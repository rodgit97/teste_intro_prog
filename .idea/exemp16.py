#calculadores
principal =0
rate =0
tempo=0

while principal <=0:
    principal = float(input("insira um numero pricipal: "))
    if principal <=0:
        print("pricipal não pode ser menor ou igual a 0")

print(principal)

while rate <=0:
    rate = float(input("insira um numero rate: "))
    if rate <=0:
        print("rate não pode ser menor ou igual a 0")

print(rate)

while tempo <=0:
    tempo = int(input("insira um numero tempo por anos: "))
    if tempo <=0:
        print("tempo não pode ser menor ou igual a 0")

print(tempo)

#total = principal * (1 + rate / 100, tempo)
#total = principal * (1 + rate / 100)
total = principal * pow(1 + rate / 100, tempo)
print(f"balança depois {tempo} ano/s: $ {total:.2f}")

print("---------------------------------------")
principal1 =0
rate1 =0
tempo1=0

while principal1 <0:
    principal1 = float(input("insira um numero pricipal: "))
    if principal1 <0:
        print("pricipal não pode ser menor a 0")

print(principal1)

while rate1 <0:
    rate1 = float(input("insira um numero rate: "))
    if rate1 <0:
        print("rate não pode ser menor ou igual a 0")

print(rate1)

while tempo1 <0:
    tempo1 = int(input("insira um numero tempo por anos: "))
    if tempo1 <0:
        print("tempo não pode ser menor ou igual a 0")

print(tempo1)

total1 = principal1 * pow(1 + rate1 / 100, tempo1)
print(f"balança depois {tempo1} ano/s: $ {total1:.2f}")

print("---------------------------------------")
principal1 =0
rate1 =0
tempo1=0

while True:
    principal1 = float(input("insira um numero pricipal: "))
    if principal1 <0:
        print("pricipal não pode ser menor a 0")
    else:
        break

print(principal1)

while True:
    rate1 = float(input("insira um numero rate: "))
    if rate1 <0:
        print("rate não pode ser menor ou igual a 0")
    else:
        break

print(rate1)

while True:
    tempo1 = int(input("insira um numero tempo por anos: "))
    if tempo1 <0:
        print("tempo não pode ser menor ou igual a 0")
    else:
        break

print(tempo1)

total1 = principal1 * pow(1 + rate1 / 100, tempo1)
print(f"balança depois {tempo1} ano/s: $ {total1:.2f}")