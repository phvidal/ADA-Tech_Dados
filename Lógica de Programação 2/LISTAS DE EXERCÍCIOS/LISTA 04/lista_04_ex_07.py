"""
Validação por blocos try except - parte 2

Quando implementamos um software, precisamos pensar nas diferentes situações que podem ocorrer nele, inclusive possíveis falhas. 
Uma falha que não seja detectada previamente pode resultar em uma interrupção abrupta do programa e esta pode ocorrer de diferentes formas.

Por exemplo, suponhamos que um programa necessite de arquitos externos para ser executado e um desses arquivos tenha sido movido para outro diretório, porém, 
o programa esteja fazendo a leitura do arquivo no diretório antigo. Quando o programa for executado, ele não encontrará o arquivo e sua execução pode ser interrompida. 
Um outro exemplo são operações matemáticas não permitidas, como uma divisão por zero.

Para evitar isso, utilizamos blocos try-except a fim de tratar possíveis erros e evitar a quebra do programa. 
Sabendo disso, implemente a função divide_dois_numeros(), que recebe dois números x e y e retorna a divisão do número x por y. 
Para garantir o uso correto, adicione um bloco try-except nesta função de forma que, caso y seja igual a zero, acione uma cláusula except ZeroDivisionError, 
além de uma segunda cláusula except para caso a função seja chamada sem um dos dois parâmetros obrigatórios (variáveis x e y), 
subindo um erro do tipo adequado (alguma built-in Exception) caso algum dos argumentos não seja passado.

"""