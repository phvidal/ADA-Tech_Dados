"""
Analisando as temperaturas do ano passado, Paulinho busca identificar quais dias houveram temperaturas médias únicas diferentes do restante dentro da mesma semana.
Dada uma lista de decimais (temperaturas) como entrada, onde existe um único número distinto nesta lista e os demais são repetidos (uma ou mais vezes), 
crie uma função para encontrar o número que é único e retorná-lo.

Ex:
Entrada: [18, 19, 20, 21, 20, 19, 18]
Saída: 21

Ex:
Entrada: [28.5, 27.9, 28.5, 27.9, 30, 28.5]
Saída: 30

def numero_unico(lista):
	### Seu código aqui

"""
def numero_unico(lista):

    for elemento in lista:
        if lista.count(elemento) == 1:
            return elemento
    None

lista = [18, 19, 20, 21, 20, 19, 18]
numero = numero_unico(lista)

print(numero)
