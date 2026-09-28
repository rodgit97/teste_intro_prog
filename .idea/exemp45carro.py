
class Carro:
    def __init__(self, modelo, ano, cor, para_venda):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.para_venda = para_venda

    def conduzir(self):
        print(f"conduz o carro {self.cor} {self.modelo}")

    def para(self):
        print(f"para o carro {self.cor} {self.modelo}")

    def descrever(self):
        print(f"{self.ano} {self.cor} {self.modelo} ")