"""
Faça uma calculadora. O usuário deve inserir qual a operação matemática ele deseja realizar e logo em seguida os dois números. O programa deve
finalizar apenas quando o usuário digitar a opção "sair" no momento de escolha da operação matemática.

"""

operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()


if operador == 'SAIR':
    print('Você saiu do sistema, até mais.')


while operador != 'SAIR':

    num_01 = float(input('Digite um número: '))
    num_02 = float(input('Digite mais um número: '))

    if operador == '+':
        print(f'A soma entre {num_01} e {num_02} é: {num_01 + num_02}')
        operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()
    elif operador == '-':
        print(f'A subtração entre {num_01} e {num_02} é: {num_01 - num_02}')
        operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()
    elif operador == '*':
        print(f'A multiplicação entre {num_01} e {num_02} é: {num_01 * num_02}')
        operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()
    elif operador == '/' and num_02 == 0:
        print('Não é possível dividir um número por ZERO')
        operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()
    elif operador == '/':
        print(f'A divisão entre {num_01} e {num_02} é: {num_01 / num_02}')
        operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()
    else:
        print('Seu operador não foi válido !')
        operador = input('Qual operação matemática deseja realizar?: "/", "*", "+" ou "-". Para sair, digite "sair".: ').upper()