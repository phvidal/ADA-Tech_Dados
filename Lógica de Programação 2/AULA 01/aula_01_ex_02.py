"""
Escreva a função chamada opera que recebe uma tupla com uma string e dois números; se a string for SOMA, 
retorna a soma dos dois números, se for MULT, retorna a multiplicação, se for DIV, retorna a divisão, se for SUB, 
retorna a subtração, se não for nenhuma das anteriores retorna None.

"""

def opera (operacao: str, x: float, y: float):
    operacao_mat = operacao
    operacao_mat = operacao_mat.upper()

    if operacao_mat == "SOMA":
        resultado = x + y
    elif operacao_mat == "MULT":
        resultado == x * y
    elif operacao_mat == "DIV":
        resultado = x / y
    elif operacao_mat == "SUB":
        resultado = x - y
    else:
        return None

    return resultado

teste = opera('SOMA', 5, 10)
print(teste)

# ALTERAR PARA RECEBER UMA TUPLA