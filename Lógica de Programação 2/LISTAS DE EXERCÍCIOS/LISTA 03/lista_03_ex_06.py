"""
MapReduce para cálculo de soma dos quadrados

Em programação, temos que pensar não apenas na implementação do código propriamente dita para execução correta da tarefa desejada, 
como também na melhor forma de realizar esta implementação. Com isso, paradigmas de programação foram criados para auxiliar o programador a pensar diferente.

Um desses paradigmas é o uso de funções de alta ordem, o que permite que realizemos diversas operações em coleções (listas, tuplas, arrays, etc) 
sem o uso de loops explicitamente.

Um dos usos mais comuns é o uso de funções reduce, responsáveis por acumular uma operação ao longo de uma coleção. 
Essa função é muito utilizada principalmente em ambientes big data juntamente com a função map.

Sabendo disso, crie uma função ger_reduce() que recebe uma lista numérica, e retorna a soma dos quadrados destes números.

Obs.: lembre-se que, em Python, devemos importar a função reduce do módulo functools!

"""