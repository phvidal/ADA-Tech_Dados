"""
Operadores

Pedrinho trabalha com vendas de carro, mensalmente ele recebe um salário fixo e comissões baseadas em suas vendas. As comissões são as seguintes

Comissões:

    5% sobre o valor total vendido no mês
    valor fixo por cada carro vendido

Faça uma função que recebe uma lista com: número de carros por ele vendidos no mês, o valor total de suas vendas no mês, seu salário fixo, 
valor fixo que ele recebe por carro vendido. Calcule e retorne qual o salário dele (salário fixo mais comissões). 
Arredondar o valor de retorno para duas casas decimais.

Ex:
Entrada: [3, 20000.00, 2000.00, 250.00]
Saída: 3750.00

Ex:
Entrada: [4,25000.00, 3500.00, 100.00]
Saída: 5150.00

def calculo_salario_com_comissao(lista):
	### Seu código aqui

"""

def calculo_salario_com_comissao(lista):
    carros_vendidos, valor_vendas, salario_fixo, valor_por_carro = lista
    comissao_fixa = carros_vendidos * valor_por_carro
    comissao_vendas = valor_vendas * 0.05
    salario_total = salario_fixo + comissao_fixa + comissao_vendas
    salario_total = round(salario_total, 2)
    return salario_total



