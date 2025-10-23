from Veiculo import Veiculo
class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem,capacidade_toneladas, eixos):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos


    def registrar_vistoria(self, motivo, multa):
        self.motivo = motivo
        self.multa = multa

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"""             
        Capacidade toneladas: {self.capacidade_toneladas}
        eixos: {self.eixos}        
        """)

