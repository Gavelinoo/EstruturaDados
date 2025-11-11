from Veiculo import Veiculo
class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem,capacidade_toneladas, eixos):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos


    def registrar_vistoria(self, motivo, multa):
        self.motivo = motivo
        self.multa = multa
        print(f"Em razao de {motivo} você obteve uma multa de {multa}")

    def exibir_informacoes(self):
        detalhes_veiculo = super().exibir_informacoes(True)
        return f"""{detalhes_veiculo}             
        Capacidade toneladas: {self.capacidade_toneladas}
        eixos: {self.eixos}        
        """

