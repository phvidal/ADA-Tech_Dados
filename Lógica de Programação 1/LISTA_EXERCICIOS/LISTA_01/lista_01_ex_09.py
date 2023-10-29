"""
Operadores
Maria está olhando o mercado de automóveis para comprar um carro novo e identificou que o preço final do veículo tem um percentual relacionado 
ao distribuidor e também um percentual de impostos. Ela deseja, então, identificar qual veículo possui os menores percentuais de imposto e também do 
distribuidor para fazer a escolha de seu carro novo.

Para ajudar Maria com a sua busca, crie uma função que receba uma lista com o preço de final de fábrica, o valor do custo com o distribuidor e o valor dos impostos. 
Ao final a função deve retornar uma lista com o percentual do custo do distribuidor e o percentual do custo com os impostos, seguindo essa ordem. 
Realizar arredondamento para duas casas decimais em relação aos dados de retorno.

Ex:
Entrada: [100000.00, 12000.00, 20000.00]
Saída: [12.00, 20.00]

Ex:
Entrada: [115500.00,25000.00, 32500.00]
Saída: [21.64, 28.14]

def calcula_custos_carro(lista):
	### Seu código aqui

"""
def calcula_custos_carro(lista):
    pf_fabrica, vc_distribuidor, vl_imposto = lista
    porcentagem_distribuidor = (vc_distribuidor / pf_fabrica) * 100
    porcentagem_impostos = (vl_imposto / pf_fabrica) * 100

    porcentagem_distribuidor = round(porcentagem_distribuidor, 2)
    porcentagem_impostos = round(porcentagem_impostos, 2)

    percentuais = [porcentagem_distribuidor, porcentagem_impostos]
    return percentuais

teste = calcula_custos_carro([100000.00, 12000.00, 20000.00])
print(teste)
