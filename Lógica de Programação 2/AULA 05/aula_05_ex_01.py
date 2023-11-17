"""
Escreva um script python (com extensão .py) que receba como parâmetros uma lista de números inteiros, e imprima a ordem inversa dos números recebidos.

Por exemplo:
Entrada: 1,3,4,5
Saída: 5,4,3,1

Para executar o script criado, use uma sintaxe similar ao exemplo abaixo:

python nome_script.py 1 3 4 5

Em que **nome_script** poderá ser o nome de sua preferência para o arquivo com extensão .py, e os elementos são os que serão trabalhados pelo script.
**Dica:** Use o pacote **sys** para manipular os parâmetros recebidos pelo script.

"""
# NÃO ENTENDI ESSE ASSUNTO DIREITO, ESTUDAR MAIS  !!!!

import sys

def reverso(*tupla):
   resultado = list(tupla[1:])
   resultado.reverse()
   return resultado

print(reverso(*sys.argv))