"""
Crie uma lista com 4 números inteiros e outra lista com 4 chaves ["nota1", "nota2", "nota3", "nota4"], e utilize a função zip para criar um dicionário 
onde a chaves seja a lista de strings notas e os valores a lista de números.

"""

notas = ["nota1", "nota2", "nota3", "nota4"]
numeros = list(range(4))
dicionario = dict(zip(notas, numeros))

print(dicionario)
