"""
Condicionais e Operadores

Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. 
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, deverá retornar -1.

Ex:
Entrada: 235
Saída: 10

Ex:
Entrada: 121
Saída: 4

def soma_algarismos(numero):
	### Seu código aqui

"""

def soma_algarismos(numero):
    entrada = numero
    saida = 0
    if numero <= 0:
        saida = -1
    else:
        entrada_str = str(entrada)
        for n in entrada_str:
            saida = saida + int(n)

    return saida

number_teste = 0
resultado = soma_algarismos(number_teste)
print(resultado)
