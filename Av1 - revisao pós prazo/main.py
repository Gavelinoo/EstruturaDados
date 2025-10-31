from Veiculo import Veiculo
from CarroPasseio import CarroPasseio
from CaminhaCarga import CaminhaoCarga


def main():
    Celta = Veiculo("Chevrolet", "1.0", "2007","21321","Preto","5000")
    print(Celta.exibir_informacoes())
    print(Celta.registrar_manutencao("Sedã","1000"))
    Kwid = CarroPasseio("Renault", "1.0", "2017","31243", "Prata", "7000", "2", "Gasolina")
    print(Kwid.exibir_informacoes())
    Kwid.calcular_depreciacao(5, 0.15)


if __name__ == "__main__":
    main()