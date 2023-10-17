"""
Faça a somatória de todos os números seguindo a sequência:

1/1+1/2+1/3+1/4+1/5+1/6+...+1/1000

"""

somatorio = 0
denominador = 1

while denominador <= 1000:
    somatorio = somatorio + 1/denominador
    denominador += 1

print(somatorio)