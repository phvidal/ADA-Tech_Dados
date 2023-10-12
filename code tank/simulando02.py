"""
2) Um parque de diversões tem 3 atrações principais: o carrossel, piscina de bolinhas e montanha-russa.
Para poder participar de uma atração a pessoa deve cumprir as seguintes condições:
Carrossel: altura mínima de 1,00m e idade mínima de 3 anos.
Piscina de bolinhas: idade entre 4 e 9 anos e máximo de 1,30m de altura.
Montanha-russa: altura mínima de 1,10m. O fiscal de cada atração verificará o ano de nascimento da pessoa e altura para liberar o acesso para uma pessoa.
Faça uma função em python que receba o ano de nascimento e altura da pessoa e informe quais as atrações que a pessoa pode participar.

"""

altura = float(input('Digite sua altura: '))
idade = int(input('Digite sua idade: '))

pode_carrossel = altura >= 1 and idade >= 3
verifica_idade_piscina = idade >= 4 and idade <= 9
pode_piscina = altura <= 1.3 and verifica_idade_piscina
pode_montanha = altura >= 1.1

if pode_carrossel:
    print('Pode carrossel')
if pode_piscina:
    print('Pode piscina')
if pode_montanha:
    print('pode montanha')


