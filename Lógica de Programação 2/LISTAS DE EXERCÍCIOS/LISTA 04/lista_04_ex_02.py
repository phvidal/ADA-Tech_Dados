"""
Validação por blocos try except - parte 3

Quando implementamos um software, precisamos pensar nas diferentes situações que podem ocorrer nele, inclusive possíveis falhas. Uma falha que não 
seja detectada previamente pode resultar em uma interrupção abrupta do programa e esta pode ocorrer de diferentes formas.

Por exemplo, suponhamos que um programa necessite de arquitos externos para ser executado e um desses arquivos tenha sido movido para outro diretório, porém, 
o programa esteja fazendo a leitura do arquivo no diretório antigo. Quando o programa for executado, ele não encontrará o arquivo e sua execução pode ser interrompida. 
Um outro exemplo são operações matemáticas não permitidas, como uma divisão por zero.

Para evitar isso, utilizamos blocos try-except a fim de tratar possíveis erros e evitar a quebra do programa. 
Podemos utilizar esses blocos juntamente também de estruturas if-else. Sabendo disso, crie uma função verifica_numero(x1) que recebe um número e, 
caso este número não seja de tipo int, retorne uma exceção de tipo TypeError("Apenas números inteiros permitidos. Digite novamente").

"""