#dictionary = collecao de chave:valor (pares)

capitais={"EUA":"Washimgton D.C.",
          "India":"Nova deli",
          "China":"beijing",
          "Russia":"Moscovo"}

print(capitais)
print(dir(capitais))
#print(help(capitais))
print(capitais.get("India"))

if capitais.get("Japao"):
    print("a capital existe")
else:
    print("a capital NÃO existe")

capitais.update( {"Alemanha":"Berlim"})
capitais.update( {"EUA":"Detroit"})
print(capitais)

capitais.pop("China")
print(capitais)

capitais.popitem()
print(capitais)

chaves = capitais.keys()
print(chaves)

for chave in capitais.keys():
    print(chave)

valores = capitais.values()
print(valores)

itens = capitais.items()
print(itens)
for chave, valor in capitais.items():
    print(f"{chave}: {valor}")
    
capitais.clear()
print(capitais)