"""
Buscando se aperfeiçoar em soletração e na identificação de caracteres nas palavras, um aluno vencedor de uma gincana de soletração teve curiosidade em 
identificar as letras não repetidas de uma palavra. Para ajudá-lo no treino, crie uma função que recebe uma palavra e retorna o índice do primeiro 
caractere não repetido desta palavra. Caso não exista caractere único na palavra em questão, retornar -1.

Ex:
Entrada: amor
Saída: 0

Ex:
Entrada: cocada
Saída: 1

"""

def primeiro_caractere_unico(palavra):
	for i, letra in enumerate(palavra):
		if palavra.count(letra) == 1:
			return i
	return -1



