"""
Faça uma função chamada conta_letras que receba uma frase digitada pelo usuário, e que seja capaz de contar a ocorrência de cada letra na frase recebida. 
Para implementar esta função, utilize dicionários.

Exemplo:

    Entrada:
        frase = "Dicionários são legais!"
    Saída:
        d=1
        i=4
        c=1
        o=3
        ...

"""

def conta_letras(frase):
  dicionario = {}
  for letra in frase.replace(' ', '').lower():
    if letra not in dicionario:
      dicionario.update({letra: 0})
      # dicionario[letra] = 0
    dicionario[letra] += 1
  return dicionario

frase = 'Bom dia, me chamo Paulo Vidal'
resultado = conta_letras(frase)
print(resultado)