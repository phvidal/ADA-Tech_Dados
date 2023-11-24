"""
Mudança do delimitador do csv

Comumente precisamos lidar com informações que já foram armazenadas em outros locais antes da execução do programa, 
como uma planilha do excel, de forma a fazer algum processamento com estas informações. Digamos, por exemplo, 
que uma empresa tenha armazenado dados sobre as vendas dos últimos 5 anos e queira saber a média anual dessas vendas, 
podemos acessar estes dados por meio da leitura de arquivos no python para, posteriormente, realizar o cálculo da média. 
Similarmente, também podemos salvar informações em arquivos no Python para acesso futuro. Utilizando o mesmo exemplo do histórico de vendas, 
podemos realizar os cálculos de média anual e salvá-lo em um arquivo para enviar para o gerente de vendas.

Sabendo disso, supondo que uma empresa armazenou seu histórico de vendas como um arquivo csv usando ", " como delimitador, 
e agora deseje salvar um novo arquivo csv cujos valores sehjam separados por "\t". Faça uma funçãoconverte_sep() que receba uma string que contenha o 
conteúdo original do csv e retorna a string do arquivo csv com o novo separador.


"""