"""
### Condicionais e Operadores

Uma professora está precisando de ajuda para calcular a nota de seus alunos utilizando critérios de avaliação com um sistema de notas ponderadas. 
Considerando que cada aluno possui 3 notas e uma nota média de exercícios, é calculado a média de aproveitamento seguindo a fórmula abaixo:

media_aproveitamento = (N1 + N2*2 + N3*3 + media_exercicios)/7

Após a obtenção de média de aproveitamento do aluno é determinado o conceito dele, conforme:

# média >= 9,0 => conceito A
# média >= 7,5 e < 9,0 => conceito B
# média >= 6,0 e < 7,5 => conceito C
# média < 6,0 => conceito D

Para ajudar a professora com a sua turma, crie uma função que receba uma lista com as notas dos alunos 
(as três primeiras notas correspondem a N1, N2 e N3, respectivamente e a última posição a médias dos exercícios) 
e calcule a média de aproveitamento e retorne o conceito que o aluno obteve.

Ex:
Entrada: [8.0, 7.0, 8.0, 8.0]
Saída: B

Ex:
Entrada: [5.0, 4.3, 8.0, 7.0]
Saída: C

def media_aproveitamento(lista):
	### Seu código aqui

"""

def media_aproveitamento(lista):
    n1, n2, n3, media_ex = lista
    media = (n1 + (n2*2) + (n3*3) + media_ex) / 7
    conceito = ''
    if media >= 9.0:
        conceito = 'A'
    elif media >= 7.0 and media <= 9.0:
        conceito = 'B'
    elif media >= 6.0 and media <= 7.5:
        conceito = 'C'
    else:
        conceito = 'D'

    return conceito


        
    return 



