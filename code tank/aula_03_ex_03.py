"""
Faça um programa que imprima a tabuada do 9 na tela (entre 1 e 10). Insira a conta, por exemplo, 9 * 1 = 9, sendo cada um dos valores em uma linha diferente.

"""

numero_tabuada = int(input('Você gostaria de saber a tabuada de qual número?.: '))

for numero in range(1, 11):
    print(f'{numero_tabuada} x {numero} = {numero_tabuada * numero}')