"""
Condicionais, Operadores
Criar uma função que receberá uma lista com com três valores que correspondem a possíveis lista de um triângulo. Na função validar se os dados
fornecidos formam um triângulo... Caso afirmativo, retornar 'Sim', do contrário, retornar 'Não'.

OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lista.

Ex:
Entrada: [2,2,5]
Saída: false

Ex:
Entrada: [3,3,5]
Saída: true

def indicador_triangulo(lista):
	### Seu código aqui

"""
def indicador_triangulo(lista):
	    
	if lista[0] < lista[1] + lista[2] and lista[1] < lista[0] + lista[2] and lista[2] < lista[0] + lista[1]:
		return 'Sim'
	else:
		return 'Não'
