"""
Usando funções geradoras, faça um programa em python que receba uma frase, e crie uma função geradora que retorne apenas as palavras que comecem com a letra "a". 
Imprima o resultado iterando do gerador.

"""

def gera_palavras(frase):
  frase = frase.lower()
#   print(frase)
  lista = frase.split(" ")
#   print(lista)

  for palavra in lista:
    if palavra.startswith('a'): # palavra[0] == 'a'
      yield palavra

frase_usuario = 'A aula de hoje está muito alegre, amanhã chamarei a atenção de todos para seguirmos com essa alegria'

resultado = gera_palavras(frase_usuario)
for x in resultado:
  print(x)