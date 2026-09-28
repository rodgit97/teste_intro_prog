from Carro import exemp45carro

#python object oriented programming

#objeto = object
#classe = class
"""
class Carro:
    def __init__(self, modelo, ano, cor, para_venda):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.para_venda = para_venda
"""

carro1 = Carro("Mustang",2024,"vermelho", False)
carro2 = Carro("Merda",2025,"Castanho", True)
carro3 = Carro("Carregador",2023,"Amarelo", True)

carro1.conduzir()
carro1.para()
"""
print(carro1)
print(carro1.modelo)
print(carro1.ano)
print(carro1.cor)
print(carro1.para_venda)
print()
print(carro2)
print(carro2.modelo)
print(carro2.ano)
print(carro2.cor)
print(carro2.para_venda)
print()
print(carro3)
print(carro3.modelo)
print(carro3.ano)
print(carro3.cor)
print(carro3.para_venda)"""

carro1.descrever()
carro3.descrever()
carro2.descrever()


