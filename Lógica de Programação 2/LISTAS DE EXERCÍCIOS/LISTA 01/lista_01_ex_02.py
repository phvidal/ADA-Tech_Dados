"""
Indexação de listas e último elemento

Uma lista possui 'n' elementos, sendo comum executarmos determinadas ações em um elemento de determinada posição. 
Por exemplo, podemos substituir o elemento da primeira posição da lista por outro valor desejado. Quando selecionamos um elemento, chamamos isto de indexação.

Sendo assim, escreva uma função ultimoElemento() em python que recebe uma lista e retorna o último elemento da lista.

"""

def ultimoElemento(listaA):
	ultimo_elemento = listaA[-1]
	return ultimo_elemento

