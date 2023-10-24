"""
Faça um código que recebe um texto contendo letras, números e espaços. 
E, passando uma palavra, ele irá verificar se essa palavra existe nesse texto, retornando True ou False.

obs: A palavra precisa ser idêntica (mas pode ter capitalização diferente). 
Encontrar um trecho dela 'dentro' de outra palavra não deve contar como existente no texto.

# texto = "Eu me chamo Joao e minha linguagem de programação favorita é python desde 2023"

# palavra_a_pesquisar = "linguagem"

# nesse exemplo o código irá retornar True. Mas se a palavra a ser pesquisada fosse lingua, iria retornar False

"""

texto_usr = 'Eu me chamo Vidal e minha linguagem de programação favorita é python desde 2023'
validacao_texto = texto_usr.upper()
texto_lista = validacao_texto.split()

palavra_a_pesquisar = 'vida'

print('Verdadeiro' if palavra_a_pesquisar.upper() in texto_lista else 'Falso')
