#default arguments

def preco_teia(lista_preco, desconto, taxa):
    return lista_preco * (1-desconto)* (1 + taxa)

#preco_teia(500, 0 , 0.05)
print(preco_teia(500, 0 , 0.05))

print("------------------------------")

def preco_teia(lista_preco, desconto=0, taxa=0.05):
    return lista_preco * (1-desconto)* (1 + taxa)

print(preco_teia(500))
print(preco_teia(500, 0.1))
print(preco_teia(500, 0.1, 0))

print("------------------------------")
import time
def conta(comeco, fim):
    for x in range(comeco, fim + 1):
        print(x)
        time.sleep(1)
    print("FEITO")
#contagem crescente
conta(0,10)

print("------------------------------")
import time
def conta( fim,comeco=0):
    for x in range(comeco, fim + 1):
        print(x)
        time.sleep(1)
    print("FEITO")
#contagem crescente
conta(10)

print("------------------------------")
import time
def conta( fim,comeco=0):
    for x in range(comeco, fim + 1):
        print(x)
        time.sleep(1)
    print("FEITO")
#contagem crescente
conta(30, 15)