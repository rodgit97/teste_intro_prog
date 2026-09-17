operator = input("operacao(+ , - , * , /): ")
num1 = float(input("digite um numero: "))
num2 = float(input("digite outro numero: "))

print(num1 + num2)

if operator == "+":
    pass
elif operator == "-":
    pass
elif operator == "*":
    pass
elif operator == "/":
    pass

print("-----------------------------")
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
print("-----------------------------")

if operator == "+":
    result = num1 + num2
    print(round(result ,3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f" operacao {operator} invalida")