# superclass Veiculo

class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        self.marca  = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem

    def exibir_informacoes(self):
        

