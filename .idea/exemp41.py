# banking program

def mostrar_balanco(balanco):
    print("----------------------")

    print(f"seu balanço é {balanco:.2f} €")
    #pass
    print("----------------------")


def depositar():
    #pass
    montante= float(input("insira o montante para depositar: "))
    if montante < 0:
        print("----------------------")

        print("não é montante valida")
        print("----------------------")

        return 0
    else:
        return montante

def retirada(balanco):
    print("----------------------")

    #pass
    montante = float(input("insira o montante para retirar: "))
    print("----------------------")

    if montante > balanco:
        print("----------------------")

        print("montante insuficiente")
        print("----------------------")

        return 0
    elif montante < 0:
        print("----------------------")

        print("tem ser maior que 0")
        print("----------------------")

        return 0
    else:
        return montante

def main():
    balanco = 0
    carregar = True

    while carregar:
        print("----------------------")
        print("programa de bancar")
        print("----------------------")
        print(" 1. mostrar balanço")
        print(" 2. depositar")
        print(" 3. retirar")
        print(" 4. sair")

        escolha = input("entrar com sua escolha (1-4)")

        if escolha == "1":
            mostrar_balanco( balanco)
        elif escolha == "2":
            balanco += depositar()
        elif escolha == "3":
            balanco -= retirada(balanco)
        elif escolha == "4":
            carregar = False
        else:
            print("----------------------")
            print("escolha invalida")
            print("----------------------")

    print("----------------------")
    print("Obrigado pelo abraço")
    print("----------------------")


if __name__ == "__main__":
    main()

