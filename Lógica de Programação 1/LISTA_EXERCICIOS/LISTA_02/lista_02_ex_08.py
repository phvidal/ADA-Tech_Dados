"""
Um professor precisa avaliar os alunos da sua turma para definir os que foram aprovados e reprovados. 
Para definir a aprovação ou reprovação são levados os seguintes critérios: 

a) Aluno deve ter uma presença igual ou superior a 60%; 
b) Aluno deve ter uma média igual ou superior a 7.

Para ajudar o professor, elabore uma função que recebe em uma lista um dict com o nome do aluno, 
a média do aluno (nota) e a quantidade de horas (faltas) que o aluno teve durante a disciplina. 
Com esses dados, a função deve calcular se o aluno foi aprovado ou reprovado. Para calcular a presença do aluno considerar que o curso teve um total de 60 horas. 
O percentual deve ser calculado considerando a seguinte relação => (Total horas - número de faltas)/Total horas * 100;

Como resultado deve ser retornado um texto informando se o aluno foi aprovado ou reprovado com o seguinte formato: 
'Nome do aluno' + está (aprovado(a) ou reprovado(a))

Ex:
Entrada: [{"nome":"João", "nota":7, "faltas";5}]
Saída: João está aprovado(a)

Ex:
Entrada: [{"nome":"Maria", "nota":7, "faltas":30}]
Saída: Maria está reprovado(a)

def avaliacao(lista):
	### Seu código aqui
"""

def avaliacao(lista):
	resultado = []

	for aluno in lista:
		nome = aluno['nome']
		nota = aluno['nota']
		faltas = aluno['faltas']

		porcentagem_presenca = ((60 - faltas) / 60) * 100

		if porcentagem_presenca >= 60 and nota >= 7:
			resultado.append(f'{nome} está aprovado(a)')
		else:
			resultado.append(f'{nome} está reprovado(a)')
	resultado = "".join(resultado)
	return resultado

    
