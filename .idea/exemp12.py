nome = input("Digite seu nome completo: ")
rsultado =len(nome)
print(rsultado)

resultado = nome.find(" ")
print(resultado)

resultado = nome.find("f")
print(resultado)

resultado = nome.find("F")
print(resultado)

resultado = nome.rfind("f")
print(resultado)

resultado = nome.rfind("o")
print(resultado)
print("--//--")
nome = nome.capitalize()
print(resultado)

resultado = nome.upper()
print(resultado)

resultado = nome.lower()
print(resultado)

resultado = nome.isdigit()
print(resultado)

resultado = nome.isalpha()
print(resultado)

print("----------------")
numero_telefone = input("nos de o numero telefone #: ")
resultado = numero_telefone.count("-")
print(resultado)

resultado = numero_telefone.replace("-"," ")
print(resultado)

numero_telefone = numero_telefone.replace("-"," ")
print(numero_telefone)

print("----------------")
nome_utilizador = input("Digite seu nome utilizador: ")

nome_utilizador.find(" ")
if len(nome_utilizador)>12:
    print("seu nome de utilizador não pode ser mais do que 12 carateres")
elif not nome_utilizador.find(" ") == -1:
    print("seu nome NÃO pode conter espaços")
else:
    print(f"bem-vindo {nome_utilizador}")

print("----------------")
nome_utilizador = input("Digite seu nome utilizador: ")

if len(nome_utilizador) > 12:
    print("seu nome de utilizador não pode ser mais do que 12 carateres")
elif not nome_utilizador.find(" ") == -1:
    print("seu nome NÃO pode conter espaços")
elif not nome_utilizador.isalpha():
    print("seu nome NÃO pode conter numeros")
else:
    print(f"bem-vindo {nome_utilizador}")