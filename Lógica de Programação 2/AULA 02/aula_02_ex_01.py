"""
Crie uma função chamada busca que receba um dicionário e um valor. A função deverá retornar uma lista com as as chaves em que o valor recebido está associado.

Exemplo:

    Entrada:
        dicionario = { "chave1": 4, "chave2": 5, "chave3": 5, "chave4": 1 }
        valor = 5
    Saída:
        ["chave2", "chave3"]

Em complemento, peça que o usuário informe cada chave e valor que será armazenado no dicionário, e também, qual valor ele deseja buscar pela função. 
O programa deverá permitir que o usuário digite 10 chaves e 10 valores e 1 valor a ser buscado.

"""

def busca(dicionario, valor):
    chaves = []
    for c, v in dicionario.items():
        if v == valor:
            chaves.append(c) # adiciona a chave

    return chaves

dicionario_usr = {}
for _ in range(10):
    chave = input('Digite um chave: ')
    valor = input('Digite um valor: ')
    dicionario_usr.update({chave:valor})

valor_procurado = input('Valor a ser buscado: ')


resultado = busca(dicionario_usr, valor_procurado)
print(resultado)




# def busca(dicionario: dict, valor: int):


# def busca(dicionario, valor):
#     dicionario_usr = dict(dicionario)
#     valor_usr = valor
#     saida = []

#     for chave in dicionario_usr:
#         if dicionario_usr[chave] == valor_usr:
#             saida.append(chave)

#     return saida

# dicionario = { "chave1": 4, "chave2": 5, "chave3": 5, "chave4": 1 }

# print(busca(dicionario, 5))

# def busca():
#   lista_chaves = []
#   lista_valores = []
#   dicionario = {}
#   saida = []
#   i = 0
#   while i < 3:
#     chave = input('Informe uma chave: ')
#     lista_chaves.append(chave)
#     valor = input('Informe um valor: ')
#     lista_valores.append(valor)
#     i += 1
#   dicionario = dict(zip(lista_chaves,lista_valores))

#   valor_usr = input('Informe um número: ')
#   for chave in dicionario:
#     if dicionario[chave] == valor_usr:
#       saida.append(chave)
#   return saida




# def dicionario_valor(dicionario, valor):
#     lista = []
#     for chave, valor_dicionario in dicionario.items():
#         if valor == valor_dicionario:
#             lista.append(chave)
#     return lista

# qtd = int(input('Quantos valores quer digitar: '))
# while qtd <= 0 or qtd > 10:
#     qtd = int(input('Quantidade invalida (entre 1 e 10) quantos valores quer digitar: '))
    
# dicionario = {}
# for i in range (0, qtd):
#     chave = input(f'Qual a {i + 1} chave: ')
#     valor = int(input(f'Qual o {i + 1} valor: '))
#     while chave in dicionario:
#         print('Chave repetida!')
#         chave = input(f'Qual a {i + 1} chave: ')
#     dicionario.update({chave: valor})

# valor = int(input('Qual valor deseja buscar: '))
# lista = dicionario_valor(dicionario, valor)
# if len(lista) == 0:
#     print ("Não tem chave com esse valor")
# else:
#     print(lista)
