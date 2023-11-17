"""
Crie um script com extensão .py para realizar as funcionalidades de uma calculadora simples. As operações desta calculadora devem ser: SOMA, SUB, MULT e DIV. 
Ainda, esta calculadora deve realizar as operações a partir de dois números informações na passagem de argumentos (usando **kwargs) do script.

Exemplo de entrada:
python calculadora.py operacao=SOMA numero1=5 numero2=6
Saída: 11

"""
# RESOLUÇÃO PROFESSOR, NÃO RODA

import sys

def calcula(dicionario: dict) -> float:
    """
        operacao (dict): chave = operacao e valor = numero inteiro
    """
    numero1 = float(dicionario["numero1"])
    numero2 = float(dicionario["numero2"])
    if dicionario["operacao"].upper() == 'SOMA':
        return numero1 + numero2
    elif dicionario["operacao"].upper() == 'SUB':
        return numero1 - numero2
    elif dicionario["operacao"].upper() == 'MULT':
        return numero1 * numero2
    elif dicionario["operacao"].upper() == 'DIV':
        return numero1 / numero2

def transforma_dicionario(*argumentos):
    operacao = {}
    for arg in argumentos:
        chave = arg.split("=")[0]
        valor = arg.split("=")[1]
        operacao[chave] = valor
    return operacao

def transforma_dicionario2(*argumentos):
    print(dict((arg.split("=")[0], arg.split("=")[1]) for arg in argumentos))
    return dict((arg.split("=")[0], arg.split("=")[1]) for arg in argumentos)

if __name__ == "__main__":
    dicionario = transforma_dicionario2(*sys.argv[1:])
    print(calcula(dicionario=dicionario))

# if __name__ == "__main__":
#     calculadora_kwargs(**dict(arg.split('=') for arg in sys.argv[1:]))