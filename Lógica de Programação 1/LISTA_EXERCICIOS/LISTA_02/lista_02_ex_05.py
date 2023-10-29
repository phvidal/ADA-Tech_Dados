"""
Substrings

Joazinho se destacou em seu colégio ao ganhar um concurso de soletração. Então, sua professora o incentivou a participar de um concurso de soletração
a nível nacional, porém o concurso é de soletração de trás para frente. Dessa forma Joazinho vai precisar se dedicar e estudar muito para 
poder ir bem no concurso. Para ajudá-lo, crie uma função que recebe uma string, inverte-a e depois separa os carracteres em uma lista que deve ser o retorno da função.

Ex:
Entrada: amor
Saída: ["r", "o", "m", "a"]

Ex:
Entrada: carro
Saída: ["o", "r", "r", "a", "c"]

def soletrando_invertido_str(palavra):
	### Seu código aqui

"""
def soletrando_invertido_str(palavra):
    palavra_separada = palavra[::-1]
    lista_letras = list(palavra_separada)
    return lista_letras