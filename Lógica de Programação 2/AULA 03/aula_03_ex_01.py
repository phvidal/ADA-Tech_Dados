"""
Faça um programa em python que receba uma frase, e crie uma lista com apenas as palavras que comecem com a letra "a". 
Caso não exista palavras que se iniciam com letra "a", imprima uma lista vazia.

"""

def lista_palavras_com_a(frase):
    # MINHA SOLUÇÃO
    # palavras = frase.split()
    # palavra_com_a = [palavra for palavra in palavras if palavra.lower().startswith('a')]
    # return palavra_com_a

    # SOLUÇÃO THIAGO TEIXEIRA
    return [palavra for palavra in frase.lower().split() if palavra.startswith("a")]

teste = "Minha casa amarela, mor, ora, palavra leatória"
resultado = lista_palavras_com_a(teste)
print(resultado)
print(type(resultado))


