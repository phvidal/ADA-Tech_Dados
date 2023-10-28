import random

# Gere um horário aleatório
hora = random.randint(0, 23)

# Lista de opções de pizzas com seus nomes e preços
menu = [
    ["Calabresa", 70],
    ["Queijo", 50],
    ["Pepperoni", 80],
    ["Marguerita", 80],
    ["Vegetariana", 70],
    ["Frango Catupiry", 90],
    ["Lombo", 85],
    ["Portuguesa", 75],
    ["Quatro Queijos", 85]
]

# Verifique se o horário está dentro do intervalo de funcionamento
if hora >= 17 or hora <= 3:

    # Cumprimento com base no horário
    if 17 <= hora < 18:
        saudacao = "Boa tarde"
    elif 18 <= hora <= 23:
        saudacao = "Boa noite"
    elif 0 <= hora <= 3:
        saudacao = "Bom dia"

    # Solicite o nome do cliente
    print(f'{saudacao}, seja bem-vindo(a) à Pizzaria Delícia. Antes de começarmos, poderia me dizer seu nome, por favor?')
    nome = input().title()
    print(f'Olá, {nome}! Agora, estarei realizando o seu atendimento!')

    escolha1 = ""
    escolha2 = ""
    escolha3 = ""

    # Pergunte se o cliente deseja ver o cardápio
    print(f'Você gostaria de consultar o nosso cardápio de pizzas antes de realizar o seu pedido?')
    escolha1 = input('Responda, por favor, "SIM" ou "NÃO": ').upper()

    # Validação da escolha
    if escolha1 not in ["SIM", "S", "NÃO", "NAO", "N"]:
        while True:
            print(f'Desculpe {nome}, mas essa não é uma opção válida.')
            escolha1 = input('Responda, por favor, "SIM" ou "NÃO": ').upper()
            if escolha1 in ["SIM", "S", "NÃO", "NAO", "N"]:
                break

    # Se o cliente deseja ver o cardápio
    if escolha1 in ["SIM", "S"]:
        print(f'Ok, {nome}. Abaixo, apresentarei o nosso cardápio.')

        # Apresente o cardápio
        print('\n---CARDÁPIO PIZZARIA DELÍCIA---')
        for index, pizza in enumerate(menu):
            sabor, preco = pizza
            dist = 20 - len(sabor)
            alin = "_" * dist
            print(f'{index + 1} - {sabor}{alin}R${preco},00')

        # Pergunte se o cliente deseja fazer um pedido
        print('\nAgora que você conhece nossas opções disponíveis, gostaria de realizar o seu pedido?')
        escolha2 = input('Responda, por favor, "SIM" ou "NÃO": ').upper()

        # Validação da escolha
        if escolha2 not in ["SIM", "S", "NÃO", "NAO", "N"]:
            while True:
                print(f'Desculpe {nome}, mas essa não é uma opção válida.')
                escolha2 = input('Responda, por favor, "SIM" ou "NÃO": ').upper()
                if escolha2 in ["SIM", "S", "NÃO", "NAO", "N"]:
                    break

    # Se o cliente não deseja ver o cardápio ou deseja fazer um pedido
    if escolha1 in ["NÃO", "NAO", "N"] or escolha2 in ["SIM", "S"]:
        # Solicite o nome completo do cliente
        print('Para realizar o seu pedido, primeiro preciso de seu nome completo.')
        nomeCompleto = input().title()

        # Solicite o endereço do cliente
        print(f'Certo, {nome}. Agora, preciso que me informe seu endereço completo, por favor.')
        endereco = input().title()

        # Solicite a forma de pagamento
        print(f'Anotado! Por fim, informe a sua forma de pagamento.')
        formaPagamento = input('Insira o número da opção desejada. (1) Dinheiro; (2) Cartão; e (3) Pix: ')

        # Validação da forma de pagamento
        if formaPagamento not in ["1", "2", "3"]:
            while True:
                print(f'Desculpe {nome}, mas essa não é uma opção válida.')
                formaPagamento = input('Insira o número da opção desejada. (1) Dinheiro; (2) Cartão; e (3) Pix: ')
                if formaPagamento in ["1", "2", "3"]:
                    break

        # Mapeamento da forma de pagamento
        match formaPagamento:
            case "1":
                formaPagamento = "Dinheiro"
            case "2":
                formaPagamento = "Cartão"
            case "3":
                formaPagamento = "PIX"

        # Lista para armazenar os pedidos
        pedido = []

        # Início do processo de anotação dos pedidos
        print('Vamos anotar os seus pedidos!')
        while True:
            sabor = input('Informe o sabor de sua pizza ou o código dela: ').title()
            saborEncontrado = False

            # Verifique se o input é um número e corresponde a um código de pizza
            if sabor.isdigit():
                sabor = int(sabor)
                if sabor in (range(1, len(menu) + 1)):
                    pedido.append(menu[sabor - 1])
                    a, b = menu[sabor - 1]
                    print(f'\nOk, adicionando uma pizza de {a.lower()} na sua lista de pedidos.')
                    saborEncontrado = True
            else:
                # Verifique se o input corresponde a um sabor de pizza
                for item in menu:
                    if sabor in item[0]:
                        pedido.append(item)
                        print(f'\nOk, adicionando uma pizza de {sabor.lower()} na sua lista de pedidos.')
                        saborEncontrado = True
                        break

            # Se o sabor não for encontrado, peça ao cliente para tentar novamente
            while not saborEncontrado:
                print('Desculpe, mas esse sabor não está no nosso cardápio.')
                sabor = input('Informe o sabor de sua pizza ou o código dela: ').title()

                # Repita o processo de verificação
                if sabor.isdigit():
                    sabor = int(sabor)
                    if sabor in (range(1, len(menu) + 1)):
                        pedido.append(menu[sabor - 1])
                        a, b = menu[sabor - 1]
                        print(f'\nOk, adicionando uma pizza de {a.lower()} na sua lista de pedidos.')
                        saborEncontrado = True
                else:
                    for item in menu:
                        if sabor in item[0]:
                            pedido.append(item)
                            print(f'\nOk, adicionando uma pizza de {sabor.lower()} na sua lista de pedidos.')
                            saborEncontrado = True
                            break

            # Pergunte se o cliente deseja incluir outra pizza em seu pedido
            print('\nDeseja incluir outra pizza em seu pedido?')
            escolha3 = input('Responda, por favor, "SIM" ou "NÃO": ').upper()

            # Validação da escolha
            if escolha3 not in ["SIM", "S", "NÃO", "NAO", "N"]:
                while True:
                    print(f'Desculpe {nome}, mas essa não é uma opção válida.')
                    escolha3 = input('Responda, por favor, "SIM" ou "NÃO": ').upper()
                    if escolha3 in ["SIM", "S", "NÃO", "NAO", "N"]:
                        break

            # Se o cliente não deseja incluir mais pizzas, saia do loop
            if escolha3 in ["NÃO", "NAO", "N"]:
                break
            else:
                continue

        # Cálculo do total de pizzas e preço total
        totalPizzas = len(pedido)
        precoTotal = 0
        saboresLidos = []
        pedidoFormatado = []

        # Calcule o preço total e a quantidade de pizzas do mesmo sabor
        for i in range(len(pedido)):
            sabor, preco = pedido[i]

            if sabor not in saboresLidos:
                saboresLidos.append(sabor)
                novoItem = [sabor, preco, 1]
                pedidoFormatado.append(novoItem)
            else:
                for j in range(len(pedidoFormatado)):
                    s,p,q = pedidoFormatado[j]
                    if s == sabor:
                        p += preco
                        q += 1
                        pedidoFormatado[j] = [s, p, q]

            precoTotal += preco

        # Imprimir a nota fiscal
        print()
        print(f"{'*' * 40}")
        pizzaria = "Pizzaria Delícia"
        align = " " * ((40 - len(pizzaria))//2)
        print(f"{align}{pizzaria}{align}")
        print(f"{'*' * 40}")
        print(f"Sabor{' ' * 20}Quant{' ' * 5}Preço")
        print(f"{'-' * 40}")
        for sabor, preco, quantidade in pedidoFormatado:
            print(f"{sabor}{' ' * (29-len(sabor))}{quantidade}{' ' * (10-len(str(preco)))}{preco}")
        print(f"{'-' * 40}")
        print(f"{'Total:':}{' ' * (29-len(str(precoTotal)))}R${precoTotal},00")
        print(f"{'-' * 40}")
        print(f"Cliente: {nomeCompleto}")
        print(f"Endereço de Entrega: {endereco}")
        print(f"Forma de Pagamento: {formaPagamento}")

    # Mensagem de agradecimento
    print(f"\n{saudacao}, {nome}. Nós da Pizzaria Delícia agradecemos o seu contato!")

else:
    # Mensagem de fora do horário de funcionamento
    print(f'Desculpe, são {hora}h e ainda não estamos atendendo. =(')
    print('Funcionamos das 17h às 3h da manhã. Por favor, volte mais tarde!')


    # Grupo 6:
    #     Allan Daniel Martins Lima
    #     Paulo Henrique Vidal
    #     Thiago Barboza
    #     Thiago Teixeira
    #
    #
    # Quando ao possível uso de funções, entendemos que o bloco responsável pela
    # validação da entrada do usuário é repetido muitas vezes ao longo do código.
    # Assim, ele poderia ser implementado como uma função que receberia a entrada
    # inserida pelo usuário, bem como os parâmetros verdadeiros para a validação,
    # realizando, assim, tal verificação.
    #
    # Também é possível fazer o uso de funções na sessão do código responsável por
    # emitir a nota fiscal com os detalhes do pedido do cliente.