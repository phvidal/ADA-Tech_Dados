"""
Adicionar elementos em listas

Quando utilizamos listas, uma das vantagens é que podemos adicionar novos elementos com o passar do tempo. 
Podemos inserir elementos tanto ao final da lista, como também em uma posição específica.

Sabendo disso, faça uma função adicionarElemento() que recebe uma lista de números e insere o número inteiro 42 no meio da lista (isto é, em sua posição central). 
Note que a posição de inserção pode variar a depender da quantidade de elementos na lista original.

def adicionarElemento(listaA):
	pass

"""
def adicionarElemento(listaA):
	if len(listaA) % 2 == 0:
		posicao_insercao = (len(listaA) / 2)
		posicao_insercao = int(posicao_insercao)
	else:
		posicao_insercao = (len(listaA) / 2) + 1
		posicao_insercao = int(posicao_insercao)
    	
	listaA.insert(posicao_insercao, 42)		
	return listaA




lista_teste = [1, 25, 36, 43, 12, 25]
resultado = adicionarElemento(lista_teste)
print(resultado)


# posicao_insercao = (len(lista_teste) / 2) + 1
# posicao_insercao = int(posicao_insercao)
# print(posicao_insercao)