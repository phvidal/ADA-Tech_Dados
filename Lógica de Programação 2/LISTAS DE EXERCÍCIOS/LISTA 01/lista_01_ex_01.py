"""
Elementos individuais de listas
Muitas vezes, precisamos acessar elementos individuais de listas, o que é possível de ser feito a partir de sua indexação.

Sabendo disso, crie uma função retornaPenultimoEQuartoElementodeLista() que recebe uma lista e retorne o quarto e o penúltimo elemento desta lista, nesta ordem.

"""

def retornaPenultimoEQuartoElementodeLista(tuplaA):
        if len(tuplaA) >= 4:
                quarto_elemento = tuplaA[3]
                penultimo_elemento = tuplaA[-2]
                return(quarto_elemento, penultimo_elemento)
        else:
                return "A lista não possui pelo menos 4 elementos."

teste = [1, 5, 6, 8, 9, 12, 36, 75]
resultado = retornaPenultimoEQuartoElementodeLista(teste)
print(resultado)
print(type(resultado))