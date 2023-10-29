"""
Paulinho está fazendo uma análise de temperatura média dos dias do último verão em sua cidade e busca semanas que possuem dias que possuem mesma temperatura média. 
Para ajudá-lo, crie uma função que recebe uma lista de valores decimais e identifique se, dentre o conjunto dos dados, existem e quantos são os valores repetidos. 
Assim, a função deve retornar a quantidade de dias com temperaturas iguais de acordo com a mensagem: 
'Sim, existem ZZ dias com temperatura média repetida.' (onde ZZ é a quantidade de registros repetidos) caso aquela lista de temperaturas possua mais de 
um dia com temperatura repetida, ou 'Não, não existem dias com temperatura média repetida.', caso não haja.

Ex:
Entrada: [27.5, 30.2, 28.5, 29, 25, 24, 25.5]
Saída: Não, não existem dias com temperatura média repetida.

Ex:
Entrada: [30.5, 30, 29.5, 30, 30.5, 31, 30]
Saída: Sim, existem 3 dias com temperatura média repetida.

"""

def elementos_repetidos(lista):
	repetidas = 0

	for i in range(len(lista)):
		for j in range(i + 1, len(lista)):
			if lista[i] == lista[j]:
				repetidas += 1
	if repetidas > 0:
		mensagem = f'Sim, existem {repetidas + 1} dias com temperatura média repetida.'
	else:
		mensagem = 'Não, não existem dias com temperatura média repetida.'

	return mensagem

lista = [27.5, 30.2, 28.5, 29, 25, 24, 25.5, 25, 29, 29]
numero = elementos_repetidos(lista)

print(numero)
