#*args & **kwargs

#nao chave chave

def soma(a,b):
    return a+b

print(soma(10,20))

print("---------------------")
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(20,20))
print(add(20,20,20))

print("---------------------")
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(3))

print("---------------------")
def ecra_nome(*args):
    for arg in args:
        print(arg, end=' ')

ecra_nome("teste", "123")
print()
print(ecra_nome("teste", 123))

print("---------------------")
#kwargs
def imprimir_endereco(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
    #pass
    #print(type(kwargs))
 #   for valor in kwargs.values():
  #      print(valor)
   # for cahve in kwargs.keys():
    #    print(cahve)


imprimir_endereco(rua= "123 r falsa",cidade= "falsopolis" , estado= "estado" , zip="12345",apt="12")

print("---------------------")
def etiqueta_envio(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    """for valor in kwargs.values():
        print(valor, end=' ')
    """
    #pass
    if "apt" in kwargs:
        print(f"{kwargs.get('rua')}, {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('rua')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('rua')}")

    print(f"{kwargs.get('cidade')}, {kwargs.get('estado')}, {kwargs.get('zip')}")

etiqueta_envio("dr.", "Abrao", "lincao" , "III",
               rua = "123 falso",
               pobox="PO BOX #1000",
               cidade = "falso",
               estado = "estado",
               zip = "12345",
               apt= "")