"""
Faça um programa em python que receba uma lista de alunos e suas respectivas notas em uma disciplina qualquer, e usando compreensão de dicionários, 
filtre apenas os alunos que obtiveram nota superior ou igual a 7.0. 
Observação: tanto os elementos da lista recebida, quanto os elementos retornados, deverão ser um dicionário.

"""

def media_alunos(nome, nota):
    alunos_nota_maior_7 = {nomes:notas for nomes, notas in zip(nome, nota) if notas >= 7}
    return alunos_nota_maior_7

teste_nomes = ['Paulo', 'Joao', 'Mariana', 'Fernando']
teste_notas = [6, 5, 8, 10]
resultado = media_alunos(teste_nomes, teste_notas)
print(resultado)

# # Função para filtrar alunos com notas >= 7.0 e criar dicionários com os alunos aprovados
# def filtrar_alunos_aprovados(alunos):
#     alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7.0]
#     return alunos_aprovados

# # Recebe a lista de alunos e suas notas
# alunos = []
# n = int(input("Quantos alunos deseja inserir? "))
# for i in range(n):
#     nome = input("Nome do aluno: ")
#     nota = float(input("Nota do aluno {}: ".format(nome))
#     aluno = {'nome': nome, 'nota': nota}
#     alunos.append(aluno)

# # Chama a função para filtrar os alunos aprovados
# alunos_aprovados = filtrar_alunos_aprovados(alunos)

# # Imprime os dicionários dos alunos aprovados
# print("Alunos aprovados com nota >= 7.0:")
# for aluno in alunos_aprovados:
#     print("Nome:", aluno['nome'], "Nota:", aluno['nota'])
