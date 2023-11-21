"""
Remoção de espaços extras de strings
É comum em sistemas de cadastro, os clientes preencherem dados com caracteres ou espaços indesejáveis. Sendo assim, 
implemente uma função remove_espaco(listaStrings) que recebe uma lista de strings e retire espaços extras que possam haver no início, meio ou no fim de uma string.

Por exemplo,

entrada: ["  string", "  exemplo  ", "do   exercício"] saída: ["string", "exemplo", "do exercício"]

"""

def remove_espacos(listaStrings):
	resultado = [' '.join(string.split()) for string in listaStrings]
	
	return resultado