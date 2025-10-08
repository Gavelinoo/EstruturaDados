menu = {
    "Mussarela": 30,
    "Calabresa": 35,
    "Marguerita": 30,
    "Frango com catupiry": 34,
    "Strogonoff": 36
}
lista = []
pedido = ""
print(f"Olá, seja bem vindo a pizzaria, nosso sabores são {menu}")
while pedido != "sair":
    pedido=input("Digite o seu sabor de pizza ")
    if pedido in menu:
        lista.append(pedido)
        print(f"Sabor de {pedido} adicionado ao pedido!")
    elif pedido not in menu:
        print("Sabor não encontrado")


## pegar o valor da chave

soma = 0
for total in lista:
    print(f"Seu pedido foi: {total}")
    soma += menu[total] ## acessando o valor da chave, através da chave do dicionário
print(f"O total do seu pedido deu: R$:{soma}")







