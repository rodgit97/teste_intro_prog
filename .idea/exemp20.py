# lists, sets, and tuples 🍎
#list
#frutas= "maça"
frutas = ["maça", "banana", "cereja"]
print(frutas)

print("------------")
#sets
frutas = ["maça", "banana", "cereja","coco"]
print(frutas)
print(frutas[0])
print(frutas[-1])
print(frutas[0:2])

for fruto in frutas:
    print(fruto)

print(dir(frutas))
print(help(frutas))
print(len(frutas))
print("maça" in frutas)
print("ananas" in frutas)

frutas[0]= "ananas"
for fruta in frutas:
    print(fruta)

frutas.append("ananas")
print(frutas)

frutas.remove("ananas")
print(frutas)

frutas.insert(0,"pingas")
print(frutas)

frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

print(frutas.index("ananas"))
print(frutas)

print(frutas.count("ananas"))

frutas.clear()
print(frutas)
print("------------")
frutas= {"uvas", "civi","amora", "aranha"}
print(frutas)
print(dir(frutas))
print(len(frutas))
print("uvas" in frutas)
#print(frutas[0])
frutas.add("aranha")
print(frutas)

frutas.remove("aranha")
print(frutas)

frutas.pop()
print(frutas)



frutas.clear()
print(frutas)


print("------------")
frutas = ("ameixa", "pera", "melão")
print(frutas)

print(dir(frutas))
print(help(frutas))
print("ameixa" in frutas)
print(frutas.index("ameixa"))

print(frutas.count("pera"))

for fruta in frutas:
    print(fruta)