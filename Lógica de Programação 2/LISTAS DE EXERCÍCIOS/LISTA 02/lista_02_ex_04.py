"""
Dicionário cujos valores são listas

Em determinadas situações, é necessário agrupar informações de acordo com alguma dada característica para facilitar o acesso a essas informações. 
Uma estrutura em python que armazena informações seguindo essa organização são dicionários.

Um exemplo de uso comum de dicionários são cadastros de clientes, em que, por exemplo, um elemento do dicionário pode ser o nome dos clientes, 
outro elemento o emprego outro o estado de habitação. Quando quisermos utilizar apenas as informações de estado, selecionamos apenas este elemento do dicionário, 
utilizando a respectiva chave como indexador do dicionário.

Sabendo disso, crie uma função mediaPrecoCelular() que receba um dicionário que possui a chave "valor", e retorne uma lista com: 
a média dos valores existentes nesta chave, o celular mais barato, e o mais caro, nesta ordem.

def mediaPrecoCelular(dictCelulares):
	pass

"""
def mediaPrecoCelular(dictCelulares):
	valores = dictCelulares["valor"]
	if len(valores) == 0:
		return None
	media = sum(valores) / len(valores)
	cel_mais_barato = min(valores)
	cel_mais_caro = max(valores)
	return [media, cel_mais_barato, cel_mais_caro]


