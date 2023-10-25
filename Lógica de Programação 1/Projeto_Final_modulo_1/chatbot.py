import random


hora = random.randint(0,23)

if hora >= 17 or hora <= 3:

    menu = [["Calabresa", 70], ["Queijo", 50], ["Pepperoni", 80], ["Marguerita", 80], ["Vegetariana", 70],
        ["Frango com Catupiry", 90], ["Lombo com Cheddar", 85], ["Portuguesa", 75], ["Quatro Queijos", 85]]

    if hora >= 17 and hora < 18:
        print("Boa tarde.")
    elif hora >= 18 and hora <= 23:
        print("Boa noite.")
    elif hora >= 0 and hora <= 3:
        print('Bom dia.')

    print('---Menu de Atendimento---')
    print('1 - Visualizar Menu')
    print('2 - Fazer Pedido')

    entrada = int(input('Digite: '))

    if entrada not in [1, 2]:
        while True:
            entrada = int(input('Digite uma opção válida: '))
            if entrada in [1, 2]:
                break

    if entrada == 1:
        print()
        print('---CARDÁPIO PIZZARIA DELÍCIA---')

    for item in range(len(menu)):
        print(f'{item + 1} - {menu[item]}')

    print()
    print('Posso anotar o seu pedido?')
    print('1 - Ainda não, mostre-me o menu de novo.')
    print('2 - Sim! Desejo iniciar o meu pedido.')

    entrada = int(input('Digite: '))

    if entrada not in [1, 2]:
        while True:
            entrada = int(input('Digite uma opção válida: '))
            if entrada in [1, 2]:
                break

    if entrada == 2:
        nome = input('Nome: ')
        end = input('Endereço: ')
        pag = int(input('Forma de Pagamento, 1. Dinheiro, 2. Cartão e 3. Pix: '))

    if pag not in [1, 2, 3]:
        while True:
            pag = int(input('Digite uma opção válida: '))
            if pag in [1, 2, 3]:
                break

    print('Pedido')
    pizza = input('Informe o sabor de sua pizza ou o código dela: ')

    # for item, preco in menu:
    #     if pizza not in menu:
    #         while True:
    #             pizza = int(input('Digite uma opção válida: '))
    #             if pizza in menu:
    #                 break

else:
    print('aaaa')

