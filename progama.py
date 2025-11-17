from funcoes import *

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
    elif menu == 2:
        adicionar_pedido(listacardapio)
    elif menu == 3:
        exibir_pedido(listacardapio)
    elif menu == 4:
        remover_item(listacardapio)
    elif menu == 0:
        print("Programa encerrado")
        break
    else:
        print('Essa opção não existe!')    