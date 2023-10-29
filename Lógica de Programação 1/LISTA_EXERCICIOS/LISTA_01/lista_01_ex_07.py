"""
Operadores

João é um empresário do ramo de construção civil e decidiu adotar novos critérios para dar reajuste salarial para seus funcionários quando completarem 
aniversário de contratação. Agora o reajuste vai ser dado seguindo as regras abaixo.

Tempo de serviço:

    de 1 até 5 anos => 1%
    de 6 até 10 anos => 1.5%
    11 ou mais anos => 2% valor da inflação (IPCA)

O valor total percentual para o reajuste vai ser a soma do percentual de tempo de serviço + o percentual da inflação

Para ajudar a João a calcular o valor do reajuste salarial de seus funcionários crie uma função que recebe uma lista como entrada contendo apenas números decimais, 
onde a posição 0 da lista é o tempo de serviço, a posição 1 é o valor da inflação e a posição 2 é o salário do funcionário. 
Sua função deve calcular o novo salário e retorná-lo. Favor considerar arredondamento de duas casas decimais para o salário retornado.

Ex:
Entrada: [1, 5.0, 2000.00]
Saída: 2120.00

Ex:
Entrada: [11, 4.5, 2500.00]
Saída: 2662.50

def calculo_salario(lista):
	### Seu código aqui
"""
def calculo_salario(lista):
	tempo_empresa, inflacao, salario_funcionario = lista
	inflacao = salario_funcionario * (inflacao / 100) #transforma o valor da inflação em porcentagem
	aumento_tempo_empresa = tempo_empresa / 100 #transforma o tempo de empresa em porcentagem   
	aumento = 0 

	if tempo_empresa < 1:
		aumento = 0
	elif tempo_empresa >= 1 and tempo_empresa <= 5:
		aumento = salario_funcionario * 0.010 
	elif tempo_empresa > 5 and tempo_empresa <= 10:
		aumento = salario_funcionario * 0.015
	else:
		aumento = salario_funcionario * 0.020

	salario_final = salario_funcionario + aumento + inflacao
	salario_final = round(salario_final, 2)

	return salario_final
        
