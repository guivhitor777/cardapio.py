
def carregar_cardapio():
    cardapio = [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
                { "id": 2,
                "nome": "Pizza",
                "preco": 30},
                { "id": 3,
                "nome": "Refrigerante",
                "preco": 5}]
    return cardapio


def exibir_cardapio(cardapio):
    return cardapio


def adicionar_pedido(cardapio, pedidos):
    id = input("digite o seu ID:")
    quantidade = int(input("digite a quantidade:"))

    for i in cardapio:
        if i["id"] == id:
            total = quantidade*i["preco"]
            nome = i["nome"]


    pedido = {"id":id,"quantidade":quantidade,"total":total,"nome":nome}
    pedidos.append(pedido)
def exibir_pedido(pedidos):
    return pedidos


def remover_item(pedidos):
    id = int(input("digite o seu ID:"))
    for i in pedidos:
        if id == 1:
            cont -= 1
        if id == 2:
            cont -= 1
        if id == 3:
            cont -= 1
