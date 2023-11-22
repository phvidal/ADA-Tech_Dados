"""
Comumente precisamos lidar com informações que já foram armazenadas em outros locais antes da execução do programa, como uma planilha do excel, 
de forma a fazer algum processamento com estas informações. 
Digamos, por exemplo, que uma empresa tenha armazenado dados sobre as vendas dos últimos 5 anos e queira saber a média anual dessas vendas. 
Podemos acessar estes dados por meio da leitura de arquivos no python para, posteriormente, realizar o cálculo da média. 
Similarmente, também podemos salvar informações em arquivos no Python para acesso futuro. 
Utilizando o mesmo exemplo do histórico de vendas, podemos realizar os cálculos de média anual e salvá-lo em um arquivo para enviar para o gerente de vendas.

Sabendo disso, crie uma função produto_mais_vendido() para ler um arquivo csv com as vendas de uma loja e retornar o nome do produto mais vendido 
(em termos de quantidades de vendas) conforme registrado no arquivo. A função receberá diretamente a string lida de um arquivo csv que usa ", " como separador. 
No arquivo, temos as seguintes colunas: data, produto, quantidade, valor.

"""

import csv
from collections import defaultdict

def produto_mais_vendido(conteudo_csv):
    # Dicionário para armazenar a quantidade total de cada produto
    quantidade_por_produto = defaultdict(int)

    # Converte a string CSV em um objeto leitor CSV
    leitor_csv = csv.reader(conteudo_csv.splitlines(), delimiter=', ')

    # Pula o cabeçalho (assumindo que a primeira linha contém os rótulos das colunas)
    next(leitor_csv, None)

    # Itera sobre as linhas do arquivo e calcula a quantidade total de cada produto
    for linha in leitor_csv:
        produto = linha[1]
        quantidade = int(linha[2])
        quantidade_por_produto[produto] += quantidade

    # Encontra o produto mais vendido
    produto_mais_vendido = max(quantidade_por_produto, key=quantidade_por_produto.get)

    return produto_mais_vendido