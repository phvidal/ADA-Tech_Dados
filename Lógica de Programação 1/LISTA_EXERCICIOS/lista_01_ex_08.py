"""
Condicionais

Maria tem uma frutaria e está com uma promoção para quem comprar mais de 10 frutas (do mesmo item). A tabela de preços das frutas com preços especiais são:

Comprando qualquer fruta da promoção e levando acima de 10 frutas o preço da unidade fica em 1.25 cada, caso a pessoa leve uma quantidade inferior 
ou igual a 10 o preço individual da fruta fica em 1.45.

Faça uma função que recebe a quantidade de frutas que o cliente está levando e calcule o valor final a ser pago. 
Arredondar o valor final da compra para 2 casas decimais.

Ex:
Entrada: 2
Saída: 2.90

Ex:
Entrada: 12
Saída: 15.00

def custo_compra(qtd_frutas):
	### Seu código aqui

"""

def custo_compra(qtd_frutas):
    entrada = qtd_frutas
    valor_pagar = 0

    if entrada <= 10:
        valor_pagar = entrada * 1.45
    else:
        valor_pagar = entrada * 1.25

    valor_pagar = round(valor_pagar, 2)
    return valor_pagar

frutas_pagas = custo_compra(12)
print(frutas_pagas)
    
        
