listacardapio = []
cont = 0
cardapio = {
    "id": 1,
    "nome": "Hambúrguer",
    "preco": 12.5,
    "id": 2,
    "nome": "Pizza",
    "preco": 30,
    "id": 3,
    "nome": "Refrigerante",
    "preco": 5,
}


def carregar_cardapio():
    return cardapio


def exibir_cardapio(listacardapio):
    return listacardapio


def adicionar_pedido(listacardapio, cardapio):
    id = input("digite o seu ID:")
    quantidade = input("digite a quantidade:")

    for i in cardapio:
        if id == 1:
            cont += 1
        if id == 2:
            cont += 1
        if id == 3:
            cont += 1


def exibir_pedido(pedido):
    return pedido


def remover_item(pedido):
    id = input("digite o seu ID:")
    for i in cardapio:
        if id == 1:
            cont -= 1
        if id == 2:
            cont -= 1
        if id == 3:
            cont -= 1
