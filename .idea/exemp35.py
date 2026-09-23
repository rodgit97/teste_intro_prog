#membership operators
palavra="apple"
letra = input("Digite uma letra secreta: ")

if letra in palavra:
    print(f"é a letra secreta: {letra}")
else:
    print(f"{letra} não foi encontrado na palavra")

print("------------------------")
if letra in palavra:
    print(f"{letra} não foi encontrado na palavra")
else:
    print(f"tem a letra: {letra}")

print("------------------------")
estudantes = {"bob", "praticio","sandra"}
estudante = input("nos de um nome de um estudante: ")
if estudante in estudantes:
    print(f"estudante: {estudante}")
else:
    print(f"NAO FOI ENCONTRADO estudante: {estudante}")

print("------------------------")
notas = {"sandra" : "A", "lula": "B", "bob":"C", "patricio":"D"}
estudantes = {"bob", "praticio","sandra"}
estudante = input("para as notas, nos de um nome de um estudante: ")
if estudante in estudantes:
    print(f"a nota do {estudante} é {notas[estudante]}")
else:
    print(f" {estudante} não foi encontrado ")

print("------------------------")
email = "rodrigo@mail.pt"

if "@" in email and "." in email:
    print(f"e-mail valido")
else:
    print(f"e-mail NAO VALIDO")