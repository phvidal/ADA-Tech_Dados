"""
Faça um código que recebe uma string e retorna todas as letras minúsculas com exceção da letra A/a.

Ex: recebe: Posso dizer que sei programar em Python.

retorna: posso dizer que sei progrAmAr em python.

"""

texto = input('Digite um texto: ')

texto_min = texto.lower().replace('a','A')

print(texto_min)

