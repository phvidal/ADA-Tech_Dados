"""
Crie a lista abaixo em uma variável chamada minha_lista. A lista abaixo contém 50 elementos variados, incluindo inteiros, float, strings, valores booleanos e até outra lista.

[1, 3.14, "Python", True, [10, 20, 30], "Lista", 42, 2.718, False, [1, 2, 3], "Variada", 7, 0.5, True, "Elementos", [100, 200, 300], "Misturados", 9, 2.0, False, "Em", [4, 5, 6], 5, 1.618, True, "Uma", [7, 8, 9], "Única", 11, 3.0, False, "Lista", [11, 12, 13], "Para", 13, 4.0, True, "Praticar", [14, 15, 16], "Python", 17, 5.0, False, "Programação", [17, 18, 19]]

Crie uma nova lista chamada sublista que contenha os elementos do índice 2 (inclusive) até o índice 7 (exclusivo).
Crie uma nova lista chamada primeiros_5 que contenha os cinco primeiros elementos da lista minha_lista
Crie uma nova lista chamada ultimos_4 que contenha os quatro últimos elementos da lista minha_lista.
Crie uma nova lista chamada sublista_2, dentro dela deverá conter:
Índice 2 e 3
Do elemento de índice 4, extraia apenas os elementos de índice 1 e 2
Do último elemento da lista principal, extraia apenas o elemento de índice 1

Refaça o exercício anterior, trazendo cada tópico como uma lista, dentro de uma lista principal, chamada de principal.

"""

minha_lista = [1, 3.14, "Python", True, [10, 20, 30], "Lista", 42, 2.718, False, [1, 2, 3], "Variada", 7, 0.5, True, "Elementos", [100, 200, 300], "Misturados", 9, 2.0, False, "Em", [4, 5, 6], 5, 1.618, True, "Uma", [7, 8, 9], "Única", 11, 3.0, False, "Lista", [11, 12, 13], "Para", 13, 4.0, True, "Praticar", [14, 15, 16], "Python", 17, 5.0, False, "Programação", [17, 18, 19]]

sublista = minha_lista[2:7]
print(f'Sublista: {sublista}')

primeiros_5 = minha_lista[:5]
print(f'Primeiros 5: {primeiros_5}')

ultimos_4 = minha_lista[-4:]
print(f'Últimos 4: {ultimos_4}')

sublista_2 = minha_lista[2:4] + minha_lista[4][1:] + [minha_lista[-1][1]]
print(f'Sublista 2: {sublista_2}')

principal = [minha_lista[2:4], minha_lista[4][1:], [minha_lista[-1][1]]]
print(f'Principal: {principal}')
print(type(principal))
