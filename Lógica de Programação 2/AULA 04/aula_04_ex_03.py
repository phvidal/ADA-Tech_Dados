"""
Faça uma função/expressão geradora em python que receba uma lista de alunos e uma lista de cursos, e retorne um dicionário por vez no formato:

{"nome": aluno, "curso" :curso}

"""
nome_aluno = ['Paulo', 'Mariana', 'Luiz', 'Nathalia', 'Larissa', 'Eduardo']
cursos = ['Python', 'Marketing', 'Engenharia', 'Publicidade', 'Javascript', 'PHP']

def gera_dicionario(nome, cursos):
    for aluno, curso in zip(nome, cursos):
        yield {'nome':aluno, 'curso':curso}

for x in gera_dicionario(nome_aluno, cursos):
    print(x)