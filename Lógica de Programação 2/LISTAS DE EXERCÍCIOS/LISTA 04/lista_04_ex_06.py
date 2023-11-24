"""
Validação por blocos try except - parte 6

Quando implementamos um software, precisamos pensar nas diferentes situações que podem ocorrer nele, 
inclusive possíveis falhas. Uma falha que não seja detectada previamente pode resultar em uma interrupção abrupta do programa e esta pode ocorrer de n formas.

Por exemplo, suponhamos que um programa necessite de arquitos externos para ser executado e um desses arquivos tenha sido movido para outro diretório, porém, 
o programa esteja fazendo a leitura do arquivo no diretório antigo. Quando o programa for executado, ele não encontrará o arquivo e sua execução pode ser interrompida. 
Um outro exemplo são operações matemáticas não permitidas, como uma divisão por zero.

Para evitar isso, utilizamos blocos try-except afim de tratar possíveis erros e evitar quebra do programa. Um erro comum de ocorrer é alguma variável 
do programa estar vazia em um dado momento quando não deveria estar. Sabendo disso, faça um programa que lance uma exceção TypeError caso uma variável seja None.

"""