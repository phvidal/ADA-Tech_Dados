"""
Modifique o programa das médias do exercício anterior da seguinte maneira:

Caso a aluna tenha ficado de exame, pergunte a nota do exame.

Uma nova média deve ser calculada entre a média original e a nota do exame:

media_exame = (media + exame)/2

O programa deve exibir essa nova média junto do novo status:

Aprovada por exame caso a media_exame seja pelo menos 50.
Reprovada caso a media_exame seja inferior a 50.

"""

nota_anterior = float(input('Digite sua média anterior: '))
nota_exame = float(input('Qual sua nota do exame?: '))
nova_media = (nota_anterior + nota_exame) / 2

if nova_media >= 50:
    print(f'Aprovado por exame, sua nota foi {nova_media}!')
else:
    print(f'Reprovado, sua média foi {nova_media} e é menor que 50')