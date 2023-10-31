"""
Escreva uma função chamada intercala que recebe duas tuplas de três elementos cada e retorna uma tupla de seis elementos intercalando as duas tuplas.

Exemplo:
Entrada: tupla1 = (1, 2, 4) tupla2 = (3, 5, 6)
Saída: (1, 3, 2, 5, 4, 6)


"""

def intercala(tupla_1, tupla_2):
    saida = ()
    tamanho_minimo = min(len(tupla_1), len(tupla_2))

    for i in range(tamanho_minimo):
        saida += (tupla_1[i], tupla_2[i])

    return saida

tp_01 = (1, 3, 5, 7)
tp_02 = (2, 4, 6)

teste = intercala(tp_01, tp_02)
print(teste)

# Solução THIAGO TEIXEIRA

# teste = intercala(tupla01, tupla02)
# print(teste)

# t1 = (0, 2, 4, 6, 8)
# t2 = (1, 3, 5, 7, 9)

# def intercala(t1, t2):
  
#   res = []

#   for a, b in zip(t1, t2):
#     res.append(a)
#     res.append(b)

#   return tuple(res)


# print(intercala(t1, t2))


