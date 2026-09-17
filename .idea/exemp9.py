unit = input("qual temperatura em celsius ou fahemheit(C/P)")
temp = float(input("dar temperatura: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32,1)
    print(f" a temperatura em fahemhenheit é: {temp} ºF")
    #pass
elif unit == "F":
    temp = round((9 * temp) / 5 + 32,1)
    print(f" a temperatura em celsius é: {temp} ºF")
    #pass
else:
    print(f"{unit} não vale de unidade")