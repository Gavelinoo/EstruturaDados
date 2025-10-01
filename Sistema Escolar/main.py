from Pessoa import Pessoa
from Professor import Professor
from Aluno import Aluno

def main():
    Jorge = Pessoa("Jorge", "35", "12345678910", "Sarapui 8", "21252781")
    Bruno = Professor("Bruno", "25", "123456788", "Rua Mexico", "2154655622", "Estrutura de dados")
    Israel = Aluno("Israel", "25", "3234123212", "Quartel", "23423234324", "123")


    Jorge.mostrar_detalhes()
    Bruno.mostrar_detalhes()
    Israel.mostrar_detalhes()


if __name__ == "__main__":
    main()