#funcao

def feliz_aniversario():# vai repetir
    print("parabens para vos")
    print("envelheceu")
    print("parabens para vos")
    print()
feliz_aniversario()
feliz_aniversario()
feliz_aniversario()

print("----------------------")

def feliz_aniversario1(nome):# vai repetir
    print(f"parabens para {nome}")
    print("envelheceu")
    print("parabens para vos")
    print()

feliz_aniversario1("rodrigo")
feliz_aniversario1("banana")
feliz_aniversario1("zé")

print("----------------------")

def feliz_aniversario(nome, idade):# vai repetir
    print(f"parabens para {nome}")
    print(f"envelheceu {idade} anos")
    print("parabens para vos")
    print()

feliz_aniversario("rodrigo", 28)
feliz_aniversario("banana", 30)
feliz_aniversario("zé",21)


print("----------------------")

def feliz_aniversario(idade, nome):# vai repetir
    print(f"parabens para {nome}")
    print(f"envelheceu {idade} anos")
    print("parabens para vos")
    print()

feliz_aniversario("rodrigo", 28)
feliz_aniversario("banana", 30)
feliz_aniversario("zé",21)

print("----------------------")

def feliz_aniversario(x, y):# vai repetir
    print(f"parabens para {x}")
    print(f"envelheceu {y} anos")
    print("parabens para vos")
    print()

feliz_aniversario("rodrigo", 28)
feliz_aniversario("banana", 30)
feliz_aniversario("zé",21)

print("----------------------")
def fatura_ecra(nome_utilizador, montante, data_devida):
    print(f"boas {nome_utilizador}")
    print(f"sua fatura de {montante:.2f} é devida {data_devida}")

fatura_ecra("rodrigofigueira", 100.10,"01/02")

print("----------------------")
#return

#z = add(1,2)
#z=3
def add(x, y):
    z = x + y
    return z
#print(z)
def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(10, 20))
print(multiply(10, 20))
print(divide(10, 20))

print("----------------------")
def criar_nome(primeiro, ultimo):
    primeiro = primeiro.capitalize()
    ultimo = ultimo.capitalize()
    return primeiro + " " + ultimo

nome_completo= criar_nome(" banana","gregorio")
print(nome_completo)