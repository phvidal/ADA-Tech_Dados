"""
Ordenando listas

Em um sistema, comumente utilizamos listas para armazenamento de dados. Entretanto, existem casos em que torna-se necessário criarmos um padrão de organização dos dados. 
Por exemplo, podemos organizar um cadastro de clientes pela idade destes usuários. Este procedimento de organização é conhecido como ordenação.

Sabendo disso, crie uma função chamada ordena_lista() que recebe uma lista de elementos e ordene-os em ordem decrescente. 
A função possui como parâmetro a lista a ser ordenada e retorna a mesma lista ordenada de forma decrescente.

def ordena_lista(listaA):
	pass

"""

def ordena_lista(listaA):
	lista_ordenada_decrescente = sorted(listaA, reverse= True)
	return lista_ordenada_decrescente
	

# lista_teste = [1, 25, 32, 13, 8, 96, 11]
# lista_ordenada = sorted(lista_teste)
# print(lista_ordenada)
# print(sorted(lista_ordenada, reverse=True))


# REPOSTANDO UM ERRO NA PLATAFORMA
# O exercício pede como resposta uma lista ordenada em forma decrescente, porém uma de suas respostas, está com um erro, ela retorna a seguinte resposta:
# [  100,   88,   32,   27,   14,   2,   5,   0 ]

# Sendo que o correto é:
# [  100,   88,   32,   27,   14,   5,  2,   0 ]