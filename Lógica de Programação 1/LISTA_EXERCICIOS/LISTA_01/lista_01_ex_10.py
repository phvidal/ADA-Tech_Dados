"""
Condicionais e Conversão

Em uma danceteria o preço da entrada sofre variações de acordo com o dia da semana. Nas Segundas, Terças e Quintas, o desconto oferecido é de 25% 
em cima do preço normal de entrada. Nos dias de músicas ao vivo, o preço da entrada tem um acréscimo de 15% em relação ao preço normal da entrada. 
Faça uma função que recebe o dia da semana, o preço normal da entrada e se é dia de música ao vivo (“sim” ou “não”).

Os valores de entrada serão passados em uma lista seguindo a ordem supracitada. Calcule e retorne o preço final que deverá ser pago pela entrada 
considerando um arredondamento de três casas para o valor final da entrada.

Obs: aplicar primeiro o desconto dos dias com desconto e depois o acréscimo de música ao vivo, quando os dois descontos forem aplicados.

A entrada dos dias da semana será considerando um valor decimal, conforme os dados a seguir:

    # 1.0 - segunda-feira
    # 2.0 - terça-feira
    # 3.0 - quarta-feira
    # 4.0 - quinta-feira
    # 5.0 - sexta-feira
    # 6.0 - sábado
    # 7.0 - domingo

Para os dados referente a música ao vivo serão considerados: 1.0 - sim e 2.0 - não.

Ex:
Entrada: [3.0, 25.00, 2.0]
Saída: 25.000

Ex:
Entrada: [4.0, 50.00, 1.0]
Saída: 43.125

def calcula_valor_entrada(lista):
	### Seu código aqui

"""
def calcula_valor_entrada(lista):
    dia_semana, valor_entrada, musica_ao_vivo = lista
    desconto_semana = [1.0, 2.0, 4.0]
    valor_com_desc = 0
    acresc_musica = 0
    if dia_semana in desconto_semana:
        valor_com_desc = (valor_entrada * 0.25)
    else:
        valor_com_desc = 0
    
    if musica_ao_vivo == 1.0:
        acresc_musica = (valor_entrada * 0.15)
    else:
        acresc_musica = 0

    valor_total = (valor_entrada - valor_com_desc) + acresc_musica
    valor_total = round(valor_total, 3)
    return valor_total

teste = calcula_valor_entrada([4.0, 50.00, 1.0])
print(teste)


