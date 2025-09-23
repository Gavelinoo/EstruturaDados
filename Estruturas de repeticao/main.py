# crie um site de compras, ate que o usuario digite sair

nome = "William"
idade = 22

print("Faça o seu pedido ou digite 'sair' para encerrar")
pedido = "" #String porque 'sair' é um texto
lista = ["Videogame", "SmartPhone", "Microondas", "Geladeira"]

while pedido.lower() != 'sair': # o lower faz com que reconheça o resultado
    pedido = input()("Digite um produto: ")
    if pedido in lista:
        print(f"{pedido} adicionado ao seu carrinho!")
    elif pedido.lower() == 'sair':
        print("Pedido encerrado")
    else:
        print("Esse produto não está na lista. Escolha outro: ")




