"""
Usando Dicionário para Calcular Quadrado de Números

Dicionários são estruturas de dados muito úteis e flexíveis, podendo, inclusive, ser construídos a partir de outras estruturas, como listas.

Sabendo disso, crie uma função dicionarioQuadrados() que receba uma lista números e gera um dicionário, 
de forma que cada chave do dicionário seja um elemento da lista e cada valor seja este elemento ao quadrado.

def dicionarioQuadrados(listaA):
	pass

"""

def dicionarioQuadrados(listaA):
	dicionario = {}
	for i in listaA:
		quadrado = i ** 2
		dicionario[i] = quadrado
	return dicionario

lista_teste = [2, 5, 10, 3]
resultado = dicionarioQuadrados(lista_teste)
print(resultado)
print(type(resultado))