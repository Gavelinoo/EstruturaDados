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
        return (f"""
            O tipo do seu veiculo é {tipo} e custo é de: {custo}
        """)

    def exibir_informacoes(self, detalhado=True):
        if detalhado:
            print(f"""
            Marca:{self.marca}
            Modelo:{self.modelo}
            Ano Fabric:{self.ano_fabricacao}
            Quilometragem:{self.quilometragem}
            Chassi:{self.chassi}
            cor:{self.quilometragem}          
            """)
        else:
            print(f"""
            Marca:{self.marca}
            Modelo:{self.modelo}
            Quilometragem:{self.quilometragem}      
            """)




        

