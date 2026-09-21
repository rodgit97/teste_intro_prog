#2D collections
frutas=["maça","banana", "laranja","coco"]
legumes=["cenouras", "batatas", "aboboras",]
carnes=["galinha", "peixe", "vaca","porco"]

mantimentos=[frutas,legumes,carnes]
print(mantimentos)

print(mantimentos[1])
print(mantimentos[1][0])

mantimentos=[["maça","banana", "laranja","coco"],legumes,carnes]
print(mantimentos)

for colecao in mantimentos:
    print(colecao)

for colecao in mantimentos:
    for comida in colecao:
        print(comida)

for colecao in mantimentos:
    for comida in colecao:
        print(comida, end = " ")
    print()

print("-------------------------")

mantimentos=(("maça","banana", "laranja","coco"),
             ("cenouras", "batatas", "aboboras"),
             ("galinha", "peixe", "vaca","porco"))

print(mantimentos)

print(mantimentos[1])
print(mantimentos[1][0])

mantimentos=[["maça","banana", "laranja","coco"],legumes,carnes]
print(mantimentos)

for colecao in mantimentos:
    print(colecao)

for colecao in mantimentos:
    for comida in colecao:
        print(comida)

for colecao in mantimentos:
    for comida in colecao:
        print(comida, end = " ")
    print()

print("-------------------------")

mantimentos=({"maça","banana", "laranja","coco"},
             {"cenouras", "batatas", "aboboras"},
             {"galinha", "peixe", "vaca","porco"})

print(mantimentos)

print(mantimentos[1])

mantimentos=[["maça","banana", "laranja","coco"],legumes,carnes]
print(mantimentos)

for colecao in mantimentos:
    print(colecao)

for colecao in mantimentos:
    for comida in colecao:
        print(comida)

for colecao in mantimentos:
    for comida in colecao:
        print(comida, end = " ")
    print()

print("-------------------------")
numero_pad = ((1,2,3,),(4,5,6,),(7,8,9,),("#",0,"*"))

for row in numero_pad:
    print(row)

for row in numero_pad:
    for num in row:
        print(num, end= " ")
    print()