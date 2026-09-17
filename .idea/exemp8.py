# weight converter
weight = float(input("informe o tamanho: "))
unit = input("quilogramas ou pesos? (q ou p)")

if unit == "q":
    weight =weight * 2.205
    unit ="lbs"
    print(f"seu tamanho é:{weight, 1} {unit}")

elif unit == "p":
    weight =weight / 2.205
    unit ="kgs"
    print(f"seu tamanho é:{weight, 1} {unit}")

else:
    print(f"{unit} não é valido")

print(f"seu tamanho é:{weight, 1} {unit}")
