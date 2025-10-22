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
        return f"""
        O tipo do seu veiculo é {tipo} e custa {custo}
    """

    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            return f"""
            Marca:{self.marca}
            Modelo:{self.modelo}
            Quilotametragem:{self.quilometragem}      
            
            """
        else:
            return f"""
            Marca:{self.marca}
            Modelo:{self.modelo}
            Ano Fabric:{self.ano_fabricacao}
            Quilotametragem:{self.quilometragem}
            Chassi:{self.chassi}
            cor:{self.quilometragem}          
            
            """



        

