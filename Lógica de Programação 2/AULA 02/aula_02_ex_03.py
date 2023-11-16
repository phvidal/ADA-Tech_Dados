"""
Escreva uma função chamada contador_palavras que receba uma frase, e retorne quantas vezes cada palavra aparece neste texto. 
Utilize dicionários para a contagem de cada palavra

"""

def conta_palavras(frase):
  dicionario = {}
  for palavra in frase.lower().split(" "):
    if palavra not in dicionario:
      dicionario.update({palavra: 0})
      # dicionario[letra] = 0
    dicionario[palavra] += 1
  return dicionario

frase = 'Boa tarde a todos, essa tarde está muito quente, todos nós precisamos nos refrescar'
resultado = conta_palavras(frase)
print(resultado)