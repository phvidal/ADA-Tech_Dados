"""DESAFIO
Escreva um programa Python que gera um número secreto aleatório entre 1 e 100 e, em seguida, solicita ao usuário que adivinhe qual é o número.
O programa deve fornecer dicas (maior/menor) após cada tentativa do usuário. 
O jogo deve continuar até que o usuário adivinhe corretamente o número secreto e quando adivinhar o número secreto a repetição deve ser interrompida. 
Registre quantas tentativas o usuário levou para acertar e exiba no final.

"""

numero_secreto = int(input('Digite um número que será adivinhado por outro usuário: '))

numero_chute = int(input('Qual é o número que você acha que está armazenado na memória?: '))
tentativa = 0

while numero_chute != numero_secreto:
    if numero_chute > numero_secreto:
        print(f'O número {numero_chute} é maior que o número secreto!')
        numero_chute = int(input('Qual é o número que você acha que está armazenado na memória?: '))
        tentativa += 1
    elif numero_chute < numero_secreto:
        print(f'O número {numero_chute} é menor que o número secreto!')
        numero_chute = int(input('Qual é o número que você acha que está armazenado na memória?: '))
        tentativa += 1
    else:
        break
        
print(f'Parabéns, o número digitado é o mesmo que o número secreto, você tentou {tentativa} vezes')