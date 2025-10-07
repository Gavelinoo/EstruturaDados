
menu = {
    "Mussarela": 30,
    "Calabresa": 35,
    "Marguerita": 30,
    "Frango com catupiry": 34,
    "Strogonoff": 36
}

pedido = ""
lista = []
while pedido != "sair":
    print(f"Olá, seja bem vindo a pizzaria, nosso sabores são {menu}")
    if pedido == "sair":

        break
    elif pedido != "sair":
        pedido = input("Olá, Digite o sabor da sua pizza: \n")
        lista.append(pedido)



