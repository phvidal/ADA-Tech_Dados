"""
Crie um código que receba um número a ser pesquisado em uma lista simples (não aninhada). 
Esse código deve ser removido da lista, considere que o código informado possa estar na lista representado como string ("1") ou int (1), ou seja, 
independente da representação ele deve ser removido. No final, retorne a lista resultante sem o código.

ex:
remover = 1
["1", 1, 456,29485,2845, 1, "1"]
[456,29485,2845]


"""
# RESPOSTA CHAT GPT
# lista = ["1", 1, 456, 29485, 2845, 1, "1", 25, 30, "25"]
# numero_a_remover = "1"

# lista_resultante = [item for item in lista if str(item) != str(numero_a_remover)]

# print(lista_resultante)

lista = ["1", 1, 456, 29485, 2845, 1, "1", 25, 30, "25"]
numero_a_remover = "1"
nova = []
i = 0

while i < len(lista):
    if str(lista[i]) != str(numero_a_remover): #aqui ta perguntando se '0' é diferente de '1'
        nova.append(lista[i])
    i += 1

print(nova)

