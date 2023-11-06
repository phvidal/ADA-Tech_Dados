"""
Slice

Apesar de utilizarmos listas para armazenar vários elementos, existem situações em que precisamos utilizar apenas parte desta lista. 
Por exemplo, podemos guardar em uma lista de 30 elementos com o registro do preço do dólar a cada dia nos últimos 30 dias. 
Posteriormente, podemos querer visualizar o custo do dólar apenas nos últimos 7 dias, para isso pegando os últimos 7 elementos da lista ao invés de 30.

Em python, quando selecionamos partes da lista, denominamos esta operação de slicing, podendo ser realizada não apenas para seleção dos últimos elementos da lista, 
como também elementos em qualquer posição da lista.

Sabendo disso, crie uma função particionarLista() em python que recebe uma lista e retorne apenas os elementos das posições 5 até 12.

"""

def particionarLista(listaA):
	lista_fatiada = listaA[5:12]
	return lista_fatiada