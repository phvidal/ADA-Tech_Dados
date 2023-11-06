"""
Expressões geradoras para tuplas

Também é possível utilizar expressão geradoras para construir tuplas. Sendo assim, crie a função getQuadrado() que recebe uma tupla de elementos numéricos, 
e retorna uma tupla com o quadrado de cada elemento da tupla original.

def getQuadrado(tuplaA):
	pass

"""

def getQuadrado(tuplaA):
	nova_tupla = ()
	for elemento in tuplaA:
		nova_tupla += (elemento ** 2,)
	return nova_tupla

teste = (1, 2, 5, 6, 8, 10)
resultado = getQuadrado(teste)
print(resultado)
print(type(resultado))