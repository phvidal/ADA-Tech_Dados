"""
Crie um script com extensão .py para realizar as funcionalidades de uma calculadora simples. As operações desta calculadora devem ser: SOMA, SUB, MULT e DIV. 
Ainda, esta calculadora deve realizar as operações a partir de dois números informações na passagem de argumentos (usando *args) do script.

Exemplo de entrada:
python calculadora.py SOMA 5 6
Saída: SOMA=11

"""
#   RESOLUÇÃO PROFESSOR // NÃO ESTÁ RODANDO

import sys

def calcula(operacao: str, numero1: str, numero2: str) -> float:
    """
        operacao (str): valores posiveis (SOMA, DIV, SUB, MULT)
        numero1 (str): inteiro de -inf a +inf
        numero2 (str): inteiro de -inf a +inf
    """
    numero1 = float(numero1)
    numero2 = float(numero2)
    if operacao.upper() == 'SOMA':
        return numero1 + numero2
    elif operacao.upper() == 'SUB':
        return numero1 - numero2
    elif operacao.upper() == 'MULT':
        return numero1 * numero2
    elif operacao.upper() == 'DIV':
        return numero1 / numero2

def transforma_args(*argumentos):
    return argumentos

# if __name__ == "__main__":
#     print(sys.argv)
#     operacao, numero1, numero2 = transforma_args(*sys.argv[1:])
#     print(operacao, numero1, numero2)
#     print(calcula(
#         numero1=numero1,
#         operacao=operacao,
#         numero2=numero2
#     ))
#     print(calcula.__doc__)