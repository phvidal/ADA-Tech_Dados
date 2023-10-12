'''
Suponha que você esteja desenvolvendo um sistema para cadastro de adoção de animais.
Crie um código de controle que peça ao usuário o peso do animal, que deve ser um valor real positivo, e a idade, valor inteiro entre 0 e 20. 
O código também deve perguntar ao usuário se o animal já foi vacinado, com respostas possíveis 'Sim' ou 'Não' 
e, caso o animal seja vacinado, o programa deve informar quantos meses se passaram desde a última vacina, que deve ser um valor positivo.
Para cada pergunta feita ao usuário, garanta que o valor fornecido é válido. 
Caso seja um valor inválido, o programa deve indicar uma inconsistência e pedir um novo valor ao usuário, até que seja validado.

'''
lista_nome = []
lista_telefone = []

continua_cadastro = True

while(continua_cadastro):
    nome = input('Nome:')
    telefone = input('Telefone:')

    lista_nome.append(nome)
    lista_telefone.append(telefone)

    leitura_continua = input('Continua cadastro?(s/n)')
    continua_cadastro = leitura_continua.upper() == 'S'

print()
for indice in range(len(lista_nome)):
    print(f'O telefone do {lista_nome[indice]} é {lista_telefone[indice]}')