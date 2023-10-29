"""
Coleções, Laços e Condicionais

Dentro dos conjuntos numéricos existem vários subconjuntos, dentre eles os subconjuntos dos números pares e números ímpares. 
Os números pares são todos os números múltiplos de 2, enquanto os números ímpares são o números não pares, logo, são os números que não são múltiplos de 2. 
Assim, se o resto da divisão do número por 2 for igual à 0, o número é considerado par. Se não é igual a 0, é considerado ímpar. 
Crie uma função que receba um lista de números inteiros, identifica os números como pares ou ímpares e retorna uma string 
informando a quantidade de pares seguido de uma vírgula e depois a quantidade de ímpares.

Ex:
Entrada: 1,2,3,6,9
Saída: 3 pares, 3 ímpares

Ex:
Entrada: 2,3,6
Saída: 2 pares, 1 ímpar

def par_e_impar(lista):
	### Seu código aqui...

"""

def par_e_impar(lista):
    numeros = lista
    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        
        if len(pares) <= 1 and len(impares) > 1:
            saida = f'{len(pares)} par, {len(impares)} ímpares'
        elif len(pares) > 0 and len(impares) <= 1:
            saida = f'{len(pares)} pares, {len(impares)} ímpar'
        elif len(pares) <= 1 and len(impares) <= 1:
            saida = f'{len(pares)} par, {len(impares)} ímpar'
        else:
            saida = f'{len(pares)} pares, {len(impares)} ímpares'
         
    return saida

teste = [1, 2, 3, 4]
resultado = par_e_impar(teste)
print(resultado)
print(type(resultado))