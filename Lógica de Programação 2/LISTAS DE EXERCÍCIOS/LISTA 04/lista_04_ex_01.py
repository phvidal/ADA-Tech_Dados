"""
Validação por blocos try except - parte 5

Quando implementamos um software, precisamos pensar nas diferentes situações que podem ocorrer nele, inclusive possíveis falhas. 
Uma falha que não seja detectada previamente pode resultar em uma interrupção abrupta do programa e esta pode ocorrer de diferentes formas.

Por exemplo, suponhamos que um programa necessite de arquitos externos para ser executado e um desses arquivos tenha sido movido para outro diretório, 
porém, o programa esteja fazendo a leitura do arquivo no diretório antigo. 
Quando o programa for executado, ele não encontrará o arquivo e sua execução pode ser interrompida. Um outro exemplo são operações matemáticas não permitidas, 
como uma divisão por zero.

Para evitar isso, utilizamos blocos try-except a fim de tratar possíveis erros e evitar a quebra do programa. 
Podemos utilizar esses blocos juntamente também de estruturas if-else. Sabendo disso, crie uma função verifica_extensao() que recebe um caminho de 
um arquivo a ser lido por um programa e valide a extensão deste arquivo. Será considerada uma extensão válida os arquivos nos formatos .jpg, .jpeg e .png, 
os demais deverão lançar uma exceção Exception("Formato inválido").


"""