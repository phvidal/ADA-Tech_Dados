"""
Muitas vezes quando estamos trabalhando com strings, pode ser bem útil usarmos compreensão de listas para processar caractere a caractere. 
Sabendo disso, crie uma função encontraConsoantes que retorna uma string com todas as consoantes (e apenas as consoantes!) de uma dada frase de input.

def encontraConsoantes(listaStrings):
	pass
    
"""

def encontraConsoantes(listaStrings):
    consoantes = ""
    for i in listaStrings:
        if i.isalpha() and i not in 'AEIOUaeiou':
            consoantes += i
    return consoantes