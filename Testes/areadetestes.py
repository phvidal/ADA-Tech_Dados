"""
Existe mais outro termo que pode ser utilizado, pass é um placeholder, ou seja, é usado como um espaço reservado ou marcador de 
posição quando você deseja criar uma estrutura de controle (como um loop, condicional, função, etc.) 
sem adicionar nenhuma funcionalidade. Ela não faz nada e é frequentemente usada temporariamente quando se está desenvolvendo código.

Placeholder == guardando espaço um código

"""

# cont = 0
# while cont < 10:
#     cont += 1
#     if cont == 5:
#         print('chegamos na condição')
#     print(cont)


lista = [12,-7,8,5,9,12,1,1,8,5,-7]

for i in lista:
  while lista.count(i) > 1:
    lista.remove(i)
print(lista)