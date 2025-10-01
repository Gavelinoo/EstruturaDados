# superclass pessoa
class Pessoa:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def mostrar_detalhes(self):
        print(f""
              f"Dados Pessoais\n"
              f"Nome: {self.nome}\n"
              f"idade: {self.idade}\n"
              f"cpf: {self.cpf}\n"
              f"endereco: {self.endereco}\n"
              f"telefone: {self.telefone}\n")

