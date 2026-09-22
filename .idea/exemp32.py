#keyword arguments
def boas_pessoal(saudacao, titulo, primeiro, ultimo):
    print(f"{saudacao} {titulo} {primeiro} {ultimo}")

boas_pessoal("bom dia", "Senhor", "rodrigo","figueira")

print("--------------------------------------")
def boas_pessoal(saudacao, titulo, primeiro, ultimo):
    print(f"{saudacao} {titulo} {primeiro} {ultimo}")

boas_pessoal("bom dia", ultimo="figueira", titulo="Senhor", primeiro="rodrigo")


print("--------------------------------------")
def boas_pessoal(saudacao, titulo, primeiro, ultimo):
    print(f"{saudacao} {titulo} {primeiro} {ultimo}")

boas_pessoal("bom dia", "Senhor", ultimo="banan", primeiro="coisinha")

print("--------------------------------------")
for x in range(1,11):
    print(x, end=" ")

print()
print("--------------------------------------")
print("1","2","3","4","5", sep="-")#separados por -


print("--------------------------------------")
def pegar_telefone(pais, area, primeiro, ultimo):
    return  f"{pais}-{area}-{primeiro}-{ultimo}"

numero_telefone = pegar_telefone(pais=1,area=123,primeiro=456,ultimo=7890)

print(numero_telefone)