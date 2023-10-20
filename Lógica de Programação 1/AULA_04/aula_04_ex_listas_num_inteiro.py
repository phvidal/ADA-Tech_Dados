"""
Faça um algoritmo que recebe uma lista encadeada de números inteiros e retorna uma lista sem repetições, ou seja, uma lista onde cada número apareça apenas uma vez.

Exemplo:

12, 5, -7, 8, 5, 9, 12, 1, 8
resposta: 12, 5, -7, 8, 9, 1


"""

lista_orig = [3 ,1, 2, 5, 5, 6, 3, 3, 8, 1, 6, 6, 9, 2, 5, -5, 10, -5, -9]
lista_sem_rep = list(set(lista_orig))

print(f'Lista original: {lista_orig}')
print(f'Essa é a lista sem repetição {lista_sem_rep}')

"""
Agora, considere que as saídas do exercício anterior devam ser:

Lista ordenada com valores únicos
Lista apenas com os valores repetidos (não consegui fazer)

"""
lista_ordenada_val_unic = sorted(lista_sem_rep)

print(f'Essa é a lista ordenada sem repetição: {lista_ordenada_val_unic}')






