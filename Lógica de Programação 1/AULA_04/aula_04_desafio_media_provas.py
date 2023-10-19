"""
Crie um código para apoiar os alunos de uma turma a calcularem a média de suas notas com base na quantidade de provas que foram realizadas.
Solicite do usuário a quantidade de provas realizada e a nota de cada prova realizada, 
caso o usuário informe uma quantidade menor ou igual a 0, retorne uma msg e peça novamente.

Por fim a saída deverá contemplar uma listas com todas as notas de provas, informando a quantidade de notas passadas e a média final. 
Caso a média final seja maior ou igual a 60 informe ao aluno que ele foi aprovado, caso contrário reprovado.

"""

qtd_provas = float(input('Digite a quantidade de provas que você realizou: '))
provas = 0
notas = []

while qtd_provas <= 0:
    print('Valor informado não aceito!')
    qtd_provas = int(input('Digite a quantidade de provas que você realizou: '))
else:
    while provas < qtd_provas:
        notas.append(float(input('Digite suas notas, uma por vez: ')))
        provas +=1
    print(notas)
    media = sum(notas) / len(notas)
    print(f'Sua média foi: {media} ')

print('Parabéns, você foi aprovado !' if media > 60 else 'Infelizmente, você foi reprovado!')





# if qtd_provas <= 0:
#     print('Valor informado não aceito!')
# elif qtd_provas > 0:
#     while provas < qtd_provas:
#         notas.append(int(input('Digite suas notas, uma por vez: ')))
#         provas +=1
#     print(notas)
#     media = sum(notas) / len(notas)
#     print(f'Sua média foi: {media} ')


    


