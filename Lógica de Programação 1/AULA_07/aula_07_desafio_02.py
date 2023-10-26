"""
Crie uma função chamada contar_palavras que recebe uma string como argumento e retorna uma lista com as palavras únicas e 
uma lista com a contagem de quantas vezes cada palavra aparece na string. Considere que as palavras são separadas por espaços e 
que a capitalização das palavras não deve afetar a contagem (ou seja, "Python" e "python" devem ser considerados iguais).

"""

def contar_palavras(texto_usr):
    palavras = texto_usr.lower().split()

    palavras_unicas = []
    contador_palavras = []

    for palavra in palavras:

        if palavra in palavras_unicas:
            i = palavras_unicas.index(palavra)
            contador_palavras[i] += 1
        else:
            palavras_unicas.append(palavra)
            contador_palavras.append(1)
        
    return palavras_unicas, contador_palavras

texto_usr = 'O mar é azul, azul é a cor do mar'
unicas, qtd = contar_palavras(texto_usr)


print(unicas)
print(qtd)



   
