"""
Da mesma forma que utilizamos a sintaxe "pythonica" de compreensão de listas, podemos fazer uma estrutura semelhante para gerar dicionários. 
Sendo assim, crie uma função mediaAlunosParaDicionario() que receba uma lista de listas, em que o primeiro elemento é uma lista com os nomes dos alunos; 
e o segundo elemento é uma lista com suas respectivas médias. Utilizando compreensão de dicionários, armazene estes dados no dicionário de forma que 
cada aluno seja a chave e sua média seja o valor.

OBS: caso a nota não esteja numérica, é necessário tratar os valores para tipos numéricos!

def mediaAlunosParaDicionario(listaAlunos):
	pass
    
"""
def mediaAlunosParaDicionario(listaAlunos):
	dicionario = {}
	nomes_alunos = listaAlunos[0]
	medias_alunos = listaAlunos[1]
	for i in range(len(nomes_alunos)):
		nome = nomes_alunos[i]
		media = medias_alunos[i]
		dicionario[nome] = media
	return dicionario

# ESSE FOI O CÓDIGO ACEITO NA PLATAFORMA
# def mediaAlunosParaDicionario(listaAlunos):
#     dicionario = {nome: float(media) for nome, media in zip(listaAlunos[0], listaAlunos[1])}
#     return dicionario
