"""
Faça um programa que mostre o fatorial de um número digitado.
Exemplo
número digitado: 5
resultado esperado: 120 

"""

numero_usuario = int(input('Digite um número.: '))
index = 1

for i in range(1, numero_usuario):
    fatorial = numero_usuario * index
    numero_usuario = fatorial
    index += 1

print(numero_usuario)