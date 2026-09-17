# or and not

temp = 20
esta_chover = True

if temp > 35 or temp < 0 or esta_chover:
    print("evento exterior foi cancelado")
else:
    print("evento exterior ainda está acessado")

print("------------------------------")
temp=20
esta_soelar = False

if temp >= 28 and esta_soelar:
    print("esta caloy la fora")
    print("esta ensolarado")
elif temp <= 0 and esta_soelar:
    print("esta frio la fora")
    print("esta ensolarado")
elif 28 > temp >0 and esta_soelar:
    print("esta morno la fora")
    print("esta ensolarado")
#print("--------//----------")
elif temp >= 28 and not esta_soelar:
    print("esta caloy la fora")
    print("esta nublado")
elif temp <= 0 and not esta_soelar:
    print("esta frio la fora")
    print("esta nublado")
elif 28 > temp >0 and not esta_soelar:
    print("esta morno la fora")
    print("esta nublado")