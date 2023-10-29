"""
Condicionais e Operadores
Uma empresa vende o mesmo produto para 3 diferentes estados. Cada estado possui uma alíquota diferente de imposto sobre o produto, conforme a tabela abaixo:

MG 7%;
SP 12%;
RJ 15%.

Faça um programa que, ao receber o valor do produto e o estado de destino do produto, calcule o preço final do produto acrescido do imposto baseado
no estado em que ele será vendido.

Considerar as seguintes restrições quanto a entrada e saída dos dados:

        Os dados de entrada serão passados em uma lista de decimais [valor do produto, estado comercializado]
        Para os dados do estado considerar 1.0 => MG, 2.0 => SP, 3.0 => RJ
        Caso seja passado um estado desconhecido retornar -1.0.
        Fazer um arredondamento de 4 casas no valor final do produto

Ex:
Entrada: [250.10, 1.0]
Saída: 267.6070

Ex:
Entrada: [220.50, 3.0]
Saída: 253.5750

"""
def valor_final_produto(lista):
	valor_produto, estado_venda = lista
	estado_venda = int(estado_venda)

	if estado_venda == 1:
		valor_produto = (valor_produto * 0.07) + valor_produto
	elif estado_venda == 2:
		valor_produto = (valor_produto * 0.12) + valor_produto
	elif estado_venda == 3:
		valor_produto = (valor_produto * 0.15) + valor_produto
	else:
		valor_produto = -1

	valor_produto = round(valor_produto, 4)

	return valor_produto