"""
Utilizando função lambda para calcular quadrado de números

Em programação, temos que pensar não apenas na implementação do código propriamente dita para execução correta da tarefa desejada, 
como também na melhor forma de realizar esta implementação. Com isso, paradigmas de programação foram criados para auxiliar o programador a pensar diferente.

Um desses paradigmas é a programação funcional, cujo objetivo é aumentar o determinismo do programa de forma que, 
caso o programa seja escalável e se torne muito grande, os desenvolvedores não percam o controle do código. 
Uma forma de fazer programação funcional é por meio de funções lambdas, também conhecidas como "funções anônimas", 
tendo esse nome porque não precisam ser declaradas com um nome.

Sabendo disso, crie uma função calcula_quadrado() que recebe uma lista e retorna os elementos desta lista ao quadrado, utilizando função lambda.

OBS: em um cenário real, a função calcula_quadrado() seria utilizada para outras funcionalidades também além da utilização da lambda, 
de forma a melhorar o determinismo do código.

OBS2: recomendável uso da função map.

"""

def calcula_quadrado(lista):
    resultado = list(map(lambda x: x**2, lista))
    return resultado

lista_teste = [1, 3, 5, 6, 4, 9]
resultado = calcula_quadrado(lista_teste)
print(resultado)