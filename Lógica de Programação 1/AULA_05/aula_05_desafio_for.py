"""
[839, 40, 562, 422, 644, 96, 642, 842, 818, 409, 419, 624, 764, 919, 657, 111, 503, 378, 945, 848, 976, 754, 799, 11, 540, 543, 492, 773, 204, 998, 162, 295, 399, 620, 834, 990, 153, 819, 660, 601, 367, 435, 453, 366, 166, 820, 822, 811, 853, 267, 688, 9, 234, 605, 381, 391, 405, 864, 341, 675, 239, 561, 431, 177, 625, 56, 914, 379, 251, 703, 11, 859, 1, 451, 222, 842, 540, 480, 136, 123, 223, 247, 679, 731, 84, 773, 426, 686, 162, 386, 28, 351, 335, 52, 557, 26, 649, 739, 671, 117]

Escreva um programa em Python que encontre o primeiro número múltiplo de 7 e 5. 
Você deve usar um loop for para percorrer os números nesse intervalo e interromper o loop quando encontrar o primeiro múltiplo de 7 e 5.

"""

lista = [839, 40, 562, 422, 644, 96, 642, 842, 818, 409, 419, 624, 764, 919, 657, 111, 503, 378, 945, 848, 976, 754, 799, 11, 540, 543, 492, 773, 204, 998, 162, 295, 399, 620, 834, 990, 153, 819, 660, 601, 367, 435, 453, 366, 166, 820, 822, 811, 853, 267, 688, 9, 234, 605, 381, 391, 405, 864, 341, 675, 239, 561, 431, 177, 625, 56, 914, 379, 251, 703, 11, 859, 1, 451, 222, 842, 540, 480, 136, 123, 223, 247, 679, 731, 84, 773, 426, 686, 162, 386, 28, 351, 335, 52, 557, 26, 649, 739, 671, 117]

for i in lista:
    if i % 7 == 0 and i % 5 == 0:
        print(f'O primeiro numero múltiplo de 7 e 5 é o: {i}')
        break
        

"""
Refaça o exercício anterior retornando da lista todos os número múltiplos de 7

"""

lista_nova = [839, 40, 562, 422, 644, 96, 642, 842, 818, 409, 419, 624, 764, 919, 657, 111, 503, 378, 945, 848, 976, 754, 799, 11, 540, 543, 492, 773, 204, 998, 162, 295, 399, 620, 834, 990, 153, 819, 660, 601, 367, 435, 453, 366, 166, 820, 822, 811, 853, 267, 688, 9, 234, 605, 381, 391, 405, 864, 341, 675, 239, 561, 431, 177, 625, 56, 914, 379, 251, 703, 11, 859, 1, 451, 222, 842, 540, 480, 136, 123, 223, 247, 679, 731, 84, 773, 426, 686, 162, 386, 28, 351, 335, 52, 557, 26, 649, 739, 671, 117]
multiplos_7 = []
for i in lista:
    if i % 7 == 0:
        multiplos_7.append(i)

print(f'Esses são os múltiplos de 7: {multiplos_7}')        