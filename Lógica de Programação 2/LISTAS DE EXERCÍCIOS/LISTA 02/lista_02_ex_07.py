"""
Encontrando números divisíveis por 7

Uma forma "pythonica" de iterarmos por listas é por meio de compreensão de listas, que substitui o uso de um laço de repetição for tal como 
implementamos tradicionalmente para a criação de novas listas.

Sabendo disso, digamos que em um sistema desejemos buscar, entre 1000 usuários, apenas aqueles cujo ID é divisível por 7. 
Faça uma função numerosDiv7() para este sistema que receba uma lista A de 1000 elementos e retorne uma lista apenas com os elementos de A que são divisíveis por 7.

OBS: Caso existam elementos repetidos na lista, a saída deverá exibir apenas os elementos únicos divisíveis por 7. 
E se não houver elementos divisíveis por 7, o programa deve retornar uma lista vazia.

"""

def numerosDiv7(listaA):
	lista_final = sorted(set(x for x in listaA if x % 7 == 0)) # O sorted já transforma em uma lista e trás em ordem, o set remove os duplicados
	return lista_final
	