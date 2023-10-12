"""
1) Escreva um programa que solicite um número inteiro e imprima na tela todos os números de 1 até o número digitado, separado por espaços.
Exemplo
número digitado: 5
resultado esperado: 1 2 3 4 5

"""

number_user = int(input('Digite um número: '))
contador = 1

while contador <= number_user:
    print(contador, end=' ')
    contador += 1