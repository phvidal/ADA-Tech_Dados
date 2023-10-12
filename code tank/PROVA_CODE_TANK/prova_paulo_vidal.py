""" i = input('Digite o número da casa: ')
print(type(i)) """

"""
restaurantes_ano = [['lata velha', 2018], ['santa oca', 2020]]

restaurantes_idade = []

for lista in restaurantes_ano:

    restaurantes_idade.append([lista[0], lista[1] - 2023])

    """

"""

num_entregas = 0
nivel = 0

while (num_entregas < 100):

    print(f"Faltam {100 - num_entregas} entregas para você mudar de nível!")

    num_entregas += 1


print("\nVocê atingiu o próximo nível!")
nivel = 1 """

"""
velocidade = 50

distancia = float(input('Qual é a distância da entrega?: '))  # código para receber como input do usuário a distância em km

tempo = (distancia / velocidade) * 60 # código que implementa a lógica do cálculo do tempo, em minutos


print(f"\nO tempo estimado de entrega é de {tempo} minutos!")

"""

id_cliente = []
inicio = input('Você deseja cadastrar os clientes? "S" para Sim ou "N" para sair: ').upper()

if inicio == 'N':
    print('Você não quer cadastrar nenhum cliente!')
else:
    while True:
        clientes = input('Qual o código do cliente? (ou "N" para sair): ').upper()
        if clientes == 'N':
            if id_cliente == []:
                print('Você não cadastrou nenhum cliente.')
            else:
                print(f'Os números foram inseridos nessa ordem: {id_cliente}')
                id_cliente.sort()
                print(f'Números em ordem crescente: {id_cliente}')
                media = sum(id_cliente) / len(id_cliente)
                print(f'Média dos valores: {media:.2f}')
                pares = [num for num in id_cliente if num % 2 == 0]
                print(f'Números pares: {pares}')                
                impares = [num for num in id_cliente if num % 2 != 0]
                print(f'Números ímpares: {impares}')
                repetidos = [num for num in id_cliente if id_cliente.count(num) > 1]
                print(f'Números repetidos: {list(set(repetidos))}')  # Usando set para remover duplicatas
                
            break
        elif clientes.isdigit():
            id_cliente.append(int(clientes))
        else:
            print('Digite um código de cliente válido (número inteiro) ou "N" para sair.')


