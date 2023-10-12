"""
Faça um programa em que o usuário digite números quaisquer e encerrará no momento em que o valor 0 seja digitado. Ao final diga qual foi o maior número digitado.

"""

num_01 = float(input('Digite um número: '))


maior_numero = 0

while num_01 != 0:
    
    if num_01 > maior_numero:
        maior_numero = num_01
    else:
        num_01 = num_01 = float(input('Digite um número: '))

print(f'O maior número digitado foi: {maior_numero}')
        