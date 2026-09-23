#match case statement
def dia_da_semana(dia):
    if dia == 1:
        return "é domingo"
    elif dia == 2:
        return "é segunda-feira"
    elif dia == 3:
        return "é terça-feira"
    elif dia == 4:
        return "é quarta-feira"
    elif dia == 5:
        return "é quinha-feira"
    elif dia == 6:
        return "é sexta-feira"
    elif dia == 7:
        return "é sabado"
    else:
        return " não é doia valido"

print(dia_da_semana(int(input("me de um dia: "))))

print("-----------------------------------------------")
def dia_da_semana(dia):
    match dia:
      case 1:
        return "é domingo"
      case 2:
        return "é segunda-feira"
      case 3:
        return "é terça-feira"
      case 4:
        return "é quarta-feira"
      case 5:
        return "é quinha-feira"
      case 6:
        return "é sexta-feira"
      case 7:
        return "é sabado"
      case _:
        return " não é doia valido"


print(dia_da_semana(int(input("me de um dia: "))))

print("-----------------------------------------------")
def e_fim_de_semana(dia):
    match dia:
      case "domingo":
        return True
      case "segunda":
        return False
      case "terca":
        return False
      case "quarta":
        return False
      case "quinta":
        return False
      case "sexta":
        return False
      case "sabado":
        return False
      case _:
        return False


print(e_fim_de_semana("domingo"))
print(e_fim_de_semana("segunda"))
print(e_fim_de_semana("terca"))

print("-----------------------------------------------")
def e_fim_de_semana(dia):
    match dia:
      case "sabado" | "domingo":
        return True
      case "segunda" | "terca" | "quarta" | "quinta" | "sexta":
        return False
      case _:
        return False


print(e_fim_de_semana("segunda"))