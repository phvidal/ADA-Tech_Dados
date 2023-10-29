def inverter_e_separar(texto):
    # Inverte a string
    texto_invertido = texto[::-1]

    # Separa os caracteres em uma lista
    lista_caracteres = list(texto_invertido)

    return lista_caracteres

# Exemplo de uso da função
entrada = "amor"
saida = inverter_e_separar(entrada)
print(saida)