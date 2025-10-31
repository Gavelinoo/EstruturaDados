from Veiculo import Veiculo
class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        self.anos_uso = anos_uso
        self.taxa_extra = taxa_extra
        depreciacao = anos_uso * taxa_extra
        print(f"Seu carro teve {anos_uso} anos de uso e sua depreciacao foi de {depreciacao}")


    # Sobreescrita de metodo = polimorfismo
    def exibir_informacoes(self):
        detalhes_veiculo =  super().exibir_informacoes()
        return f""" {detalhes_veiculo}
        "Qtde Portas:{self.numero_portas}
    Tipo combustivel:{self.tipo_combustivel}  
     
    """


