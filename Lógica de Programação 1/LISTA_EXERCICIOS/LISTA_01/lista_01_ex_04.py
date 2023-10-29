"""
Um certo dia Joãozinho chegou em casa e perguntou para sua mãe quantos dias ele tinha de vida... 
Sua mãe disse que ela tinha que parar para fazer a conta. Para ajudar a mãe de Joãozinho, crie uma função que recebe a idade expressa em 
anos, meses e dias (os dados de entradas estarão contidos em uma lista) e retorne a idade da pessoa expressa em dias. 
Considerar o ano como tendo um total de 365 dias, e o mês como tendo um total de 30 dias.

Ex:
Entrada: [5, 4, 14]
Saída: 1959

Ex:
Entrada: [10, 8, 16]
Saída: 3906

def idade_em_dias(lista):
	### Seu código aqui.

"""

def idade_em_dias(idade):
    anos, meses, dias = idade
    return anos * 365 + meses * 30 + dias

idade = [5, 4, 14]
idade_joao = idade_em_dias(idade)
print(idade_joao)