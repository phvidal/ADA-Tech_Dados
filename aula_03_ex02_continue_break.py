"""
Escreva um programa em Python que solicita ao usuário inserir uma sequência de números inteiros.
O programa deve continuar pedindo números até que o usuário escolha parar. 
Após cada número inserido, o programa deve verificar se o número é par. 
Se for par, incremente um contador e continue pedindo por mais números. 
No final, o programa deve exibir a quantidade total de números pares inseridos.
O usuário deve digitar 0 para sair do loop

"""

num_usr = int(input('Insira um número ou 0 para sair: '))
contador = 0
while num_usr != 0:
    if num_usr % 2 == 0:
        num_usr = int(input('Insira um número ou 0 para sair: '))
        contador += 1
    elif num_usr % 2 != 0:
        num_usr = int(input('Insira um número ou 0 para sair: '))
        continue
else:
    print(f'Você digitou um total de {contador} números pares')