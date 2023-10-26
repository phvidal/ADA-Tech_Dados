"""
A série de Fibonacci é uma sequência matemática que começa com 0 e 1, e os números subsequentes são a soma dos dois números anteriores. 
A sequência começa da seguinte forma:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Faça um programa que gere a série até que o valor seja maior que um valor informado pelo usuário. Informe quando o valor ultrapassar o valor informado pelo usuário.

"""

numero_usr = int(input('Digite um número: '))
fibonacci = 0
contador = 0
soma = 1

while numero_usr > fibonacci:
    fibonacci = fibonacci + soma
    contador += 1
    soma = contador

print(f'O número que o usuário digitou foi: {numero_usr}')
print(f'O Fibonacci ultrapassou o número do usuário alcançando o número: {fibonacci}, para isso precisou executar {contador} operações de adição.')

#arrumar o código pois está dobrando, e tem que somar o último com o penúltimo! 