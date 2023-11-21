"""
Filtrando elementos por funções lambda

Em programação, temos que pensar não apenas na implementação do código propriamente dita para execução correta da tarefa desejada, 
como também na melhor forma de realizar esta implementação. Com isso, paradigmas de programação foram criados para auxiliar o programador a pensar diferente.

Um desses paradigmas é a programação funcional, cujo objetivo é aumentar o determinismo do programa de forma que, 
caso o programa seja escalável e se torne muito grande, os desenvolvedores não percam o controle do código. 
Uma forma de fazer programação funcional é por meio de funções lambdas, também conhecidas como "funções anônimas", 
tendo esse nome porque não precisam ser declaradas com um nome.

Sabendo disso, crie uma função filtraElementos() que recebe uma lista e utiliza função lambda para filtrar os elementos maiores que 10, ou seja, 
a função deve retornar uma lista apenas com estes elementos maiores que 10.

OBS: em um cenário real, a função filtraElementos() seria utilizada para outras funcionalidades também além da utilização da lambda, 
de forma a melhorar o determinismo do código.

"""

def filtraElementos(lista):
    resultado = [x for x in lista if x > 10]
    return resultado

minhaLista = [5, 12, 8, 15, 3, 20, 7]
solucao = filtraElementos(minhaLista)
print(solucao)