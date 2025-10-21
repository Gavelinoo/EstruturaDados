from Veiculo import Veiculo
class CarroPasseio(Veiculo)
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        self.anos_uso = anos_uso
        self.taxa_extra = taxa_extra
        taxa = taxa_extra * anos_uso

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Qtde Portas:{self.numero_portas} combustivel{self.tipo_combustivel}")


