"""
DESAFIO
Imprima os seguintes padrões utilizando loop. O usuário deverá determinar quão grande será a extensão/comprimento
padrão I:

*
**
***
****

padrão II:

*
**
***
**
*
"""

#PADRÃO 1
num_estrelas = int(input('Qual a quantidade de estrelas você deseja imprimir: '))
cont = 0

while cont < num_estrelas:
    cont += 1
    print('*' * cont)

#PADRÃO 2

num_estrelas_02 = int(input('Qual a quantidade de estrelas você deseja imprimir: '))
cont_02 = 0

while cont_02 < num_estrelas_02:
    cont_02 += 1
    print('*' * cont_02)
else:
    while cont_02 > 1:
        cont_02 -= 1
        print('*' * cont_02)
