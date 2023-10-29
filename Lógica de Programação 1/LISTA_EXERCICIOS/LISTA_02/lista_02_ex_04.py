"""
Busca e Ordenação
No dia a dia é comum trabalharmos com conjuntos de dados e em casos específicos pode ser necessário o uso de algum padrão de organização para 
melhor entender os dados, como ordem alfabética, por exemplo.

Crie uma função que recebe uma lista de dados (inteiros), faz a ordenação dos dados de forma crescente e retorna o conjunto dos dados ordenados. 
A função deverá ser criada seguindo a estrutura abaixo:

def ordena(lista):
	###seu código aqui.

    
OBS: Tanto o parâmetro de entrada como o de saída da função devem ser do tipo list


"""

def ordena(lista):
	lista_ordenada = sorted(lista)
	return lista_ordenada

