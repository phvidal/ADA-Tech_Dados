"""
Operações Aritméticas

Uma professora decidiu premiar os melhores alunos de sua turma com um brinde. Para isso ela vai entregar um brinde para todos os alunos que tiverem uma 
média superior a média da turma.

Para ajudar o professor elabore uma função que recebe uma lista dos alunos em formato de dict (dicionário) com nome do aluno e a média do aluno. 
Esta função deve calcular a média da turma, identificar quais alunos tem média igual ou superior a média da turma e retornar uma lista com o nome dos 
alunos que possuem média igual ou superior a média da turma. A ordem dos nomes da lista de retorno deve obedecer a ordem da lista de entrada.

Ex:
Entrada: [{ "nome": "Maria", "nota": 7 },{"nome": "Marta", "nota": 5 },{"nome": "Marcia", "nota": 5.5 }]
Saída: [Maria]

Ex:
Entrada: [{ "nome": "Joao", "nota": 7 },{"nome": "Lucas", "nota": 5 },{"nome": "Maria", "nota": 0 },{"nome": "Marcia", "nota": 5.5 }]
Saída: [Joao, Lucas, Marcia]

def melhores_alunos(lista):
	### Seu código aqui


"""

def melhores_alunos(lista):

    # Calcula a média da turma
    media_turma = sum(nome['nota'] for nome in lista) / len(lista)

    # Filtra os alunos com média igual ou superior à média da turma
    alunos_acima_media = [nome['nome'] for nome in lista if nome['nota'] >= media_turma]

    return alunos_acima_media