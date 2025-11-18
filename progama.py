from funcoes import *
lista = []
cardapio = carregar_cardapio()
while True:
    print("Bem-vindo!")
    print("Aqui estão suas opções:")
    print("1 - Ver cardápio")
    print("2 - Adicionar item ao pedido")
    print("3 - Ver pedido")
    print("4 -  Remover item")
    print("0 - Finalizar")
    menu = int(input("Escolha uma opção: "))
    if menu == 1: 
        print(cardapio)
    if menu == 2:
        adicionar_pedido(cardapio, lista)
    if menu == 3:
        exibir_pedido(lista)
    if menu == 4:
        remover_item(lista)
    if menu == 0:
        print("Programa encerrado")
        break
    if not menu:
        print("Essa opção não existe!")    