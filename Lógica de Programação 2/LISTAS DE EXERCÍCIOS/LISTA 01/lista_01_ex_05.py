"""
Função zip

Em programação, podemos fazer uso de diferentes listas para armazenar nossos dados para, posteriormente, unir informações destas listas. 
Por exemplo, podemos guardar em uma lista os nomes de funcionários de uma empresa e, em outra lista, os cargos que estes funcionários ocupam.

funcionarios = ["Paulo", "Andrea", "Marta"]
profissao = ["cientista de dados", "engenheiro de dados", "desenvolvedor"]

Dado essas duas listas, podemos querer exibir as duas informações conjuntamente da seguinte forma:
[('Paulo', 'cientista de dados'), ('Andrea', 'engenheiro de dados'), ('Marta', 'desenvolvedor')]

Podemos fazer isto por meio da função zip que recebe as duas listas e retorna uma saída como exposta acima. 
Além de exibir os valores, podemos fazer uso da função zip para diversas funcionalidades. 
Sabendo disso, crie uma função ultimoElementoLista2D() que receba uma lista de duas dimensões (isto é, uma lista de listas, na forma de matriz) 
e utilize o zip para retornar o último elemento de cada sublista.

Por exemplo, se tivermos a lista abaixo:
[[192, 193, 194], [507, 508, 509], [526, 527, 528, 529], [560, 561], [635, 636, 637]]

Retorne [194, 509, 529, 561, 637]

"""

def ultimoElementoLista2D(listaA):
	return [sublista[-1] for sublista in listaA]

lista_teste = [[192, 193, 194], [507, 508, 509], [526, 527, 528, 529], [560, 561], [635, 636, 637]]
print(ultimoElementoLista2D(lista_teste))

# Código mais detalhado:
# def ultimoElementoLista2D(lista2D):
#     # Inicializamos uma lista vazia para armazenar os últimos elementos de cada sublista.
#     ultimos_elementos = []

#     # Percorremos cada sublista na lista de duas dimensões.
#     for sublista in lista2D:
#         # Obtemos o último elemento de cada sublista usando [-1] e o adicionamos à lista de últimos elementos.
#         ultimo_elemento = sublista[-1]
#         ultimos_elementos.append(ultimo_elemento)

#     # Retornamos a lista de últimos elementos.
#     return ultimos_elementos

# # Exemplo de uso:
# lista = [[192, 193, 194], [507, 508, 509], [526, 527, 528, 529], [560, 561], [635, 636, 637]]
# resultado = ultimoElementoLista2D(lista)
# print(resultado)
