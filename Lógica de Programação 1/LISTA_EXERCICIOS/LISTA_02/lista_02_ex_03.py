"""
Substrings

Uma escola está programando uma gincana entre os seus alunos. Um dos desafios solicita a identificação de palavras que são substring dentro de um grupo de strings, 
ou seja, quais palavras estão contidas dentro de outras palavras.

Para ajudar aos alunos crie uma função que recebe uma lista de palavras e retorna uma lista com as palavras que são substring de qualquer outra string 
existente na lista. No retorno, as substrings devem ser ordenadas de acordo com a disposição na lista de entrada, aparecendo uma única vez. 
Caso não existam substrings, a função deve retornar uma lista vazia.

Ex:
Entrada: ["as", "mas", "amor", "amoreco"]
Saída: ["as", "amoreco"]

Ex:
Entrada: ["carro","ca", "paz", "pá"]
Saída: ["ca"]

def substring_str(lista):
	### Seu código aqui

"""

def substring_str(lista):
    substrings = set() #evita as duplicadas
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[i] in lista[j]:
                    substrings.add(lista[i])

    substrings_ordenadas = [palavra for palavra in lista if palavra in substrings]

    return substrings_ordenadas

