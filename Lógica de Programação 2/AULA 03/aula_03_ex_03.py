"""
Ampliando um pouco a resolução do exercício anterior, faça um programa em python que receba uma lista de alunos e suas respectivas notas em uma disciplina qualquer, 
e usando compreensão de listas, e classifique os alunos de acordo com suas respectivas notas. 
Se o aluno obtiver nota superior ou igual a 7.0, classifique-o como aprovado. Caso contrário, classifique-o como reprovado. 
Observação: tanto os elementos da lista recebida, quanto os elementos retornados, deverão ser um dicionário.

"""

# def media_alunos(nome, nota):
#     alunos_nota_maior_7 = {nomes:notas for nomes, notas in zip(nome, nota) if notas >= 7}
#     return alunos_nota_maior_7

def situacao_alunos(nome, nota):
    return {aluno:"aprovado" if nota >= 7 else "reprovado" for aluno, nota in zip(nome, nota)} 


teste_nomes = ['Paulo', 'Joao', 'Mariana', 'Fernando']
teste_notas = [6, 5, 8, 10]
resultado = situacao_alunos(teste_nomes, teste_notas)
print(resultado)

   