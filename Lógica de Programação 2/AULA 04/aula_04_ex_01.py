"""
Usando expressões geradoras, faça um programa em python que receba uma frase, e crie uma expressão geradora que retorne apenas as palavras que comecem com a letra "a". Imprima o resultado iterando do gerador.

"""

frase_usr = 'A aula de hoje está muito complicada, amanhã precisarei estudar com mais atenção'
frase = frase_usr.lower().split()
gerador = (palavra for palavra in frase if palavra[0] == 'a')

palavras_iniciadas_em_a = []
for i in gerador:
    palavras_iniciadas_em_a.append(i)


print(palavras_iniciadas_em_a)

