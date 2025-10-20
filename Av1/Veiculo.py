# superclass Veiculo

class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        self.marca  = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem

    def registrar_manutencao(self, tipo, custo):
        self.tipo = tipo
        self.custo = custo

    def exibir_informacoes(self):
        return self.tipo
        return self.custo


        

