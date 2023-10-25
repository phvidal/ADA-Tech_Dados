"""
Imagine que você está criando um chatbot para a Pizzaria que Delícia, onde o funcionamento da pizzaria é de 17h às 3h da manhã. 
Os clientes podem fazer pedidos de pizzas disponíveis. O chatbot interagirá com os clientes, perguntando o sabor da pizza desejada e confirmará o preço, 
caso a pizza escolhida esteja no menu. O chatbot também será capaz de lidar com pedidos de múltiplas pizzas, calcular o valor total do pedido e fornecer uma 
lista final de pizzas pedidas e o valor total.

*Carregue o menu abaixo em uma lista*

Menu com pizzas disponíveis:

| Nome da pizza | Preço |
| ------------- | ----- |
| Calabresa     | 70 |
| Queijo        | 50 |
| Pepperoni     | 80 |
| Margherita    | 80 |
| Vegetariana   | 80 |

#### Atendimento
    - Incie o atendimento ao cliente com uma mensagem de boas vindas.
      - A saudação deverá respeitar a seguinte regra:
          - Quando a hora for menor que 18 - Boa tarde
          - Quando a hora estiver entre 18 e 23 (ambos inclusive) - Boa noite
          - Quando a hora estiver entre 0 e 3 (ambos inclusive) - Bom dia
      - Use o código que está na sessão DADOS INCIAIS para gerar a hora.
    - Após a mensagem de boas vindas apresente o menu de atendimento, que deve ter 2 opções
        - Visualizar Menu
        - Fazer Pedido

#### Visualizar Menu
    - Ao selecionar essa opção o menu deve ser apresentado ao usuário de modo amigável e de fácil leitura
    - A apresentação do menu de vir seguida de uma mensagem perguntando ao usuário se ele já escolheu a pizza, dando duas opções de resposta, 
    sendo uma para iniciar o pedido e outra para sair do chat.

#### Pedidos
    - Inicie o pedido perguntando os dados do cliente
      - Nome do cliente
      - Endereço do cliente
      - Forma de pagamento (Dinheiro, Cartão ou Pix)
    - Em seguida receba o pedido do cliente
    - Verifique se a pizza escolhida está disponível no menu.
        - Caso verdadeiro, confirme o preço da pizza.
        - Caso falso, informe que não está no menu e peça que escolha outra opção
    - Continue perguntando ao cliente se deseja fazer outro pedido.
    - Quando o cliente não quiser fazer mais pedidos, encerre o loop.
    - Ao final do pedido, exiba um resumo com as pizzas pedidas e o valor total do pedido. Use os dados do cliente para ter uma interação maior.


"""

import random

hora_pedido = random.randint(0,23)
atendimento = False

if hora_pedido > 3 and hora_pedido < 17:
    print(f'Olá, agora são {hora_pedido:.2f} horas, estamos fechados no momento. Por favor, retornar entre 17:00hs e 03:00hs, até mais!')
else:
    atendimento = True

pizzas = ['Calabresa', 'Queijo', 'Pepperoni', 'Margherita', 'Vegetariana']
valores = [70, 50, 80, 80, 80]
nome_cliente = ''

while atendimento:
    nome_cliente = input('Digite seu nome: ')
    if hora_pedido >= 17 and hora_pedido <= 18:
        menu_inicial = int(input(f'Boa tarde {nome_cliente}, nosso atendimento está se iniciando ás {hora_pedido}!\nPara verificar nosso menu, digite 1, para fazer um pedido, digite 2: '))
    elif hora_pedido > 18 and hora_pedido <= 23:
        menu_inicial = int(input(f'Boa noite {nome_cliente} nosso atendimento está se iniciando ás {hora_pedido}!\nPara verificar nosso menu, digite 1, para fazer um pedido, digite 2: '))
    elif hora_pedido >= 0 and hora_pedido <= 3:
        menu_inicial = int(input(f'Bom dia {nome_cliente} nosso atendimento está se iniciando ás {hora_pedido}!\nPara verificar nosso menu, digite 1, para fazer um pedido, digite 2: '))
    else:
        break
    while atendimento:
        if menu_inicial == 1:
            print(pizzas[0], valores[0], pizzas[1], valores[1], pizzas[2], valores[2], pizzas[3], valores[3], pizzas[4], valores[4])
            menu_inicial = 2
        elif menu_inicial == 2:
            pedido_cliente = True
        else:
            print(f'Você escolheu uma opção incorreta')
            menu_inicial = int(input('Para verificar nosso menu, digite 1, para fazer um pedido, digite 2: '))



    





