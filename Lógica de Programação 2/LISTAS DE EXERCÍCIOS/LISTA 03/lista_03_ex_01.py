"""
Total de vendas a partir de dados em arquivo

Comumente precisamos lidar com informações que já foram armazenadas em outros locais antes da execução do programa, como uma planilha do excel, 
de forma a fazer algum processamento com estas informações. 
Digamos, por exemplo, que uma empresa tenha armazenado dados sobre as vendas dos últimos 5 anos e queira saber a média anual dessas vendas. 
Podemos acessar estes dados por meio da leitura de arquivos no python para, posteriormente, realizar o cálculo da média. Similarmente, 
também podemos salvar informações em arquivos no Python para acesso futuro. 
Utilizando o mesmo exemplo do histórico de vendas, podemos realizar os cálculos de média anual e salvá-lo em um arquivo para enviar para o gerente de vendas.

Sabendo disso, crie uma função media_vendas() para ler um arquivo csv e retornar o total de vendas no período. 
A função receberá diretamente a string lida de um arquivo csv que usa ", " como separador. 
No arquivo, temos as seguintes colunas: data, produto, quantidade, valor. Note que a coluna "valor" corresponde ao preço unitário de cada produto, 
não o valor total da compra. Nosso objetivo é calcular o total de vendas, considerando todos os produtos registrados no arquivo.

Obs.: arredonde a resposta final para duas casas decimais.

"""

import csv

def media_vendas(vendas):
    # Inicializa o total de vendas
    total_vendas = 0.0

    # Converte a string CSV em um objeto leitor CSV
    leitor_csv = csv.reader(vendas.splitlines(), delimiter=', ')

    # Pula o cabeçalho (assumindo que a primeira linha contém os rótulos das colunas)
    next(leitor_csv, None)

    # Itera sobre as linhas do arquivo e calcula o total de vendas
    for linha in leitor_csv:
        quantidade = int(linha[2])
        valor_unitario = float(linha[3].replace(',', '.'))  # Substitui ',' por '.' para tratar números decimais
        total_vendas += quantidade * valor_unitario

    # Arredonda o resultado para duas casas decimais
    total_vendas = round(total_vendas, 2)

    return total_vendas