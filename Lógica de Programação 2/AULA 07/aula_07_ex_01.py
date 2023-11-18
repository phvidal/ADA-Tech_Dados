"""
Faça um programa que solicite ao usuário 2 números inteiros. A seguir, calcule e mostre a divisão do primeiro pelo segundo. 
Obrigatório a inclusão do bloco try-except nas leituras (ValueError) e no cálculo da divisão (ZeroDivisionError). 
O programa deve ter também a cláusula "finally" com a mensagem "FIM!!". Atenção: O programa só continua se não houver erro.

"""

try:
    num_01_usr = int(input('Digite um número: '))
    num_02_usr = int(input('Digite um número: '))   

    divisao = num_01_usr / num_02_usr

    print(f'A divisão entre {num_01_usr} e {num_02_usr} é: {divisao}')
except ValueError:
    print("Erro: Digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: não é permitido dividir nenhum número por zero !")
finally:
    print('FIM')

